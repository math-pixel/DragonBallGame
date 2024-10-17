from src.Characteres import *
from src.tools import *

class Arene:

    def __init__(self, playerWarrior:WarriorProtocol, botWarrior:WarriorProtocol):
        self.playerWarrior = playerWarrior
        self.botWarrior = botWarrior


    def showWelcome():
        print(" ----------------------------------- ")
        print(" ------ WELCOME TO THE ARENA  ------ ")
        print(" ----------------------------------- ")

    def playerTurnFight(self):
        # list les action possible
        FORM.display("Choisis une Action :", ["Utiliser un object ","Attaquer ","Ce Transformer"], [ None, self.showAttackTypeMenu, None])

    def showAttackTypeMenu(self):
        FORM.display("Choisis le type de ton attack :", ["<-- Back","simple Attaquer","Attack Special"], [ self.playerTurnFight, self.showSimpleAttackMenu, None])

    def showSimpleAttackMenu(self):
        nameAttackArray = []
        actionAttackArray = []
        nameAttackArray.append("<-- Back")
        actionAttackArray.append(self.showAttackTypeMenu)
        for i in self.playerWarrior.attack:
            nameAttackArray.append(i.__class__.__name__)
            actionAttackArray.append(i.attack())
        FORM.display("Choisis une attack :", nameAttackArray , actionAttackArray)
        
        

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