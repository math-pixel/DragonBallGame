from src.Characteres import *
from src.tools import *
import random

class FightTurn():

    PLAYER = "p"
    BOT = "b"


# Interface de l'Observateur
class Observer:
    def update(self, type:str = None, message:str = None):
        pass

class Arena(Observer):

    def __init__(self, playerWarrior:WarriorProtocol, botWarrior:WarriorProtocol, fightTurn:FightTurn = FightTurn.PLAYER):
        self.playerWarrior = playerWarrior
        self.botWarrior = botWarrior
        self.fightManager = FightManager(playerWarrior, botWarrior, fightTurn)
        self.fightManager.add_observer(self)
        self.initArena()

    def initArena(self):
        print(" ----------------------------------- ")
        print(" ------ WELCOME TO THE ARENA  ------ ")
        print(" ----------------------------------- ")
        self.fightManager.startTurn()

    def update(self,  type = None, message = None):
        print(f"New Message : {type} - {message}")
        match type:
            case "Exit Arena":
                self.playerWarrior.changeState(BasicState())
                self.botWarrior.changeState(BasicState())
                print("--------------------")
                print("---- Exit Arena ----")
                print("--------------------")

class FightManager():

    def __init__(self, warrior:WarriorProtocol, bot:WarriorProtocol, fightTurn:FightTurn = FightTurn.PLAYER):
        self.warrior = warrior
        self.bot = bot
        self.turn = fightTurn
        self.turnManager = WarriorTurnManager(self.warrior, self.bot)
        self.observerListener = []

    def fightCanContinue(self):

        print("-- stat")
        print(f"Player life : {self.warrior.life}")
        print(f"bot life : {self.bot.life}")

        if self.warrior.isAlive() == False : # warrior is dead
            return False
        elif self.bot.isAlive() == False: # bot is dead
            return False
        else:
            return True
        
    def startFight(self):
        while self.fightCanContinue():
            self.startTurn()
    
    def startTurn(self):
        # Start and toggle turn

        if self.turn == FightTurn.PLAYER:
            print("----- Your turn -----")
            self.turnManager.startPlayerTurn()
            self.turn = FightTurn.BOT
        else:
            print("----- Bot turn -----")
            self.turnManager.startBotTurn()
            self.turn = FightTurn.PLAYER

        # check if the combat can continue
        if self.fightCanContinue():
            self.startTurn()
        else:
            self.exitArena()

    def exitArena(self):
        self.notify_observers("Exit Arena", self.turn)


    def add_observer(self, observer):
        self.observerListener.append(observer)

    def remove_observer(self, observer):
        self.observerListener.remove(observer)

    def notify_observers(self, type, message):
        for observer in self.observerListener:
            observer.update(type, message)


        


class WarriorTurnManager:

    def __init__(self, playerWarrior:WarriorProtocol, botWarrior:WarriorProtocol):
        self.playerWarrior = playerWarrior
        self.botWarrior = botWarrior

    # ------------------------------- Player action ------------------------------ #
    def startPlayerTurn(self):

        # apply les effet du perso
        self.playerWarrior.applyStateEffect()
            # list les action possible
        if not isinstance(self.playerWarrior.state, ParalyzedState):
            FORM.display("Choisis une Action :", ["Utiliser un object ","Attaquer ","Ce Transformer"], [ self.showItemsMenu, self.showAttackTypeMenu, None])
        else:
            print("Vous etes paralysé et vous ne pouvez pas attaquer ce tour-ci.")
            print(f"tour restant {self.playerWarrior.state.duration}")
            FORM.display("Choisis une Action :", ["Utiliser un object ","Passer son tour"], [self.showItemsMenu, self.skipTurn])

    # -------------------------------- Attack Menu ------------------------------- #
    def showAttackTypeMenu(self):
        FORM.display("Choisis le type de ton attack :", ["<-- Back","simple Attaquer","Attack Special"], [ self.startPlayerTurn, self.showSimpleAttackMenu, self.showSpecialAttackMenu])

    def showSimpleAttackMenu(self):
        nameAttackArray = []
        actionAttackArray = []
        nameAttackArray.append("<-- Back")
        actionAttackArray.append(self.showAttackTypeMenu)
        for i in self.playerWarrior.attack:
            nameAttackArray.append(i.__class__.__name__)
            actionAttackArray.append(lambda : i.attack(self.playerWarrior, self.botWarrior))
        FORM.display("Choisis une attack :", nameAttackArray, actionAttackArray)

    def showSpecialAttackMenu(self):
        nameAttackArray = []
        actionAttackArray = []
        nameAttackArray.append("<-- Back")
        actionAttackArray.append(self.showAttackTypeMenu)
        for i in self.playerWarrior.attackSpe:
            nameAttackArray.append(i.__class__.__name__)
            actionAttackArray.append(lambda : i.attack(self.playerWarrior, self.botWarrior))
        FORM.display("Choisis une attack :", nameAttackArray, actionAttackArray)

        
    # --------------------------------- item Menu -------------------------------- #
    def showItemsMenu(self):
        nameitemsArray = []
        actionitemsArray = []

        nameitemsArray.append("<-- Back")
        actionitemsArray.append(self.startPlayerTurn)

        for i in self.playerWarrior.items:
            nameitemsArray.append(i.__class__.__name__)
            actionitemsArray.append(lambda : i.use(self.playerWarrior))

        FORM.display("Choisis un items :", nameitemsArray, actionitemsArray)

    # -------------------------------- Bot Action -------------------------------- #
    def startBotTurn(self):
        # apply les effet du perso
        self.botWarrior.applyStateEffect() 
        if not isinstance(self.botWarrior.state, ParalyzedState):
            # Define possible actions for the bot
            possible_actions = [
                self.botSimpleAttack,    # Normal attack
                self.botSpecialAttack,   # Special attack
                self.botUseItem          # Use an item (if implemented)
            ]
            
            # Randomly choose an action
            chosen_action = random.choice(possible_actions)
            chosen_action()
        else:
            print("Le bot est paralysé et passe son tour.")

    def botSimpleAttack(self):
        attack = random.choice(self.botWarrior.attack)
        print(f"Le bot utilise {attack.__class__.__name__} pour attaquer.")
        attack.attack(self.botWarrior, self.playerWarrior)

    def botSpecialAttack(self):
        if self.botWarrior.attackSpe:
            attackSpe = random.choice(self.botWarrior.attackSpe)
            print(f"Le bot utilise {attackSpe.__class__.__name__} pour attaquer.")
            attackSpe.attack(self.botWarrior, self.playerWarrior)
        else:
            print("Le bot n'a pas d'attaque spéciale disponible, il utilise une attaque simple.")
            self.botSimpleAttack()

    def botUseItem(self):
        if self.botWarrior.items:
            item = random.choice(self.botWarrior.items)
            print(f"Le bot utilise {item.__class__.__name__}.")
            item.use(self.botWarrior)
        else:
            print("Le bot n'a pas d'objet disponible, il attaque à la place.")
            self.botSimpleAttack()

    def skipTurn():
        pass

# -- combat
# choisir entre 
# - utiliser un objet 
#   -- btn --
#   retour
#   par attaque
# - Attaquer 
#   -- btn --
#   retour
#   par attaque
# - Transformation
#   -- bouton -- 
#   - retour
#   - par transformation