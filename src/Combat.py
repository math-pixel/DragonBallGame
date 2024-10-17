from src.Characteres import *
from src.tools import *


class FightTurn():

    PLAYER = "p"
    BOT = "b"

class Arena():

    def __init__(self, playerWarrior:WarriorProtocol, botWarrior:WarriorProtocol, fightTurn:FightTurn = FightTurn.PLAYER):
        self.fightManager = FightManager(playerWarrior, botWarrior, fightTurn)
        self.initArena()

    def initArena(self):
        print(" ----------------------------------- ")
        print(" ------ WELCOME TO THE ARENA  ------ ")
        print(" ----------------------------------- ")
        self.fightManager.startTurn()

class FightManager():

    def __init__(self, warrior:WarriorProtocol, bot:WarriorProtocol, fightTurn:FightTurn = FightTurn.PLAYER):
        self.warrior = warrior
        self.bot = bot
        self.turn = fightTurn
        self.turnManager = WarriorTurnManager(self.warrior, self.bot)

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
            # exitArena()
            print("exit arena")

        


class WarriorTurnManager:

    def __init__(self, playerWarrior:WarriorProtocol, botWarrior:WarriorProtocol):
        self.playerWarrior = playerWarrior
        self.botWarrior = botWarrior

    # ------------------------------- Player action ------------------------------ #
    def startPlayerTurn(self):
        # list les action possible
        FORM.display("Choisis une Action :", ["Utiliser un object ","Attaquer ","Ce Transformer"], [ None, self.showAttackTypeMenu, None])

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

    # -------------------------------- Bot Action -------------------------------- #
    def startBotTurn(self):
        print("#BOT ACTION#")

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