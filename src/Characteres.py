from src.StateCharactere import *
from src.Attacks import *
from src.Items import *

class Race():

    SAIYEN = "saiyen"
    ANDROID = "android"
    NAMEKIANS = "namekians"

class WarriorFactory():
    def __init__(self):
        pass

    def createWarrior(self, race:Race):
        match race:
            case Race.SAIYEN:
                return Warrior(SaiyenState(), [PunchAttack()], [PunchCharged()], [SenzuBeam()])
            case Race.ANDROID:
                return Warrior(AndroidState(), [PunchAttack()], [PunchCharged()], [SenzuBeam()])
            case Race.NAMEKIANS:
                return Warrior(NamekiansState(), [PunchAttack()], [PunchCharged()], [SenzuBeam()])

class Warrior():

    def __init__(self,initial_state, attacks, attackSpe, items, description = ""):
        self.stateTransformation = initial_state

        self.name = ""

        self.attack:list[AttackStandard] = attacks
        self.attackSpe:list[AttackSpe] = attackSpe

        self.stateCombat:StateWarrior = BasicState()
        self.items:list[ItemProtocol] = items

        self.level:int = 0
        self.xp:int = 0
        self.description:str = description

    def checkLevelUp(self):
        if self.xp >= 10 and self.xp < 20:
            self.level = 1
            print("----- You have unlocked a new transformation ------")
        elif self.xp >= 20 and self.xp < 30:
            self.level = 2
            print("----- You have unlocked a new transformation ------")

    def showStats(self):
        print(self.life, self.mana, self.race, self.attack, self.attackSpe, self.stateCombat, self.items, self.level, self.xp, self.allTransformation, self.unlockTransformation, self.description)

    def showPresentation(self):
        noms_items = [item.__class__.__name__ for item in self.items]
        attackList = [att.__class__.__name__ for att in self.attack]
        attackSpeList = [attSpe.__class__.__name__ for attSpe in self.attackSpe]
        print(f"Salut {self.name},\ntu as {self.stateTransformation.life} de vie et {self.stateTransformation.mana} de mana\ntu as ces attack : {', '.join(attackList)}\ntu as ces attack spe: {', '.join(attackSpeList)}\ntu as ces items : { ', '.join(noms_items)}.")

    def isAlive(self):
        return self.stateTransformation.life > 0
    
    def upgradeWarrior(self,xpEarn, life = None, mana = None, attack = None, attackSpe = None):
        
        print("------ Result of Training ------")

        self.xp += xpEarn
        self.checkLevelUp()
        
        if(life != None):
            self.stateTransformation.life += life
            print(f"life + {life}")

        if(mana != None):
            self.stateTransformation.mana += mana
            print(f"mana + {mana}")

        if(attack != None):
            self.attack.append(attack)
            print(f"yay a new attack : {attack}")

        if(attackSpe != None):
            self.attackSpe.append(attackSpe)
            print(f"yay a new special attack : {attackSpe}")

        print("--------------------------------")

    def applyStateEffect(self):
        # applique leffet au guerrier
        self.stateCombat.applyEffect(self)

    def changeState(self, newState:StateWarrior): # state of combat
        self.stateCombat = newState

    def addItem(self, item:ItemProtocol):
        self.items.append(item)

    def removeItem(self, itemIndex:int):
        self.items.pop(itemIndex)

    def setStateEvolution(self, state):
        self.stateTransformation = state

    def evolve(self):
        self.setStateEvolution(self.stateTransformation.getEvolve())

    def canTransform(self):
        if self.stateTransformation.getEvolve() != None and self.level >= self.stateTransformation.getEvolve().levelRequired:
            return True
        return False

# ---------------------------------------------------------------------------- #
#                                    Builder                                   #
# ---------------------------------------------------------------------------- #

class WarriorBuilder():

    def __init__(self, warrior:Warrior):
        self.warrior = warrior

    def addAttack(self, attack):
        self.warrior.attack.append(attack)
        return self

    def addAttackSpe(self, attack):
        self.warrior.attackSpe.append(attack)
        return self

    def addItem(self, item):
        self.warrior.items.append(item)
        return self

    def setDescription(self, description):
        self.warrior.description = description
        return self

    def setName(self, name):
        self.warrior.name = name
        return self

# ---------------------------------------------------------------------------- #
#                                TRANSFORMATION                                #
# ---------------------------------------------------------------------------- #

class TransformationState():
    def __init__(self):
        pass

    def getEvolve(self):
        pass
class SaiyenState(TransformationState):

    def __init__(self):
        self.constMaxLife = 20
        self.life = self.constMaxLife
        self.mana = 50
        self.attackPower = 5
        self.levelRequired = 0

    def getEvolve(self):
        return SuperSaiyenState()

class NamekiansState(TransformationState):

    def __init__(self):
        self.constMaxLife = 30
        self.life = self.constMaxLife
        self.mana = 10
        self.attackPower = 2
        self.levelRequired = 0


    def getEvolve(self):
        return SuperNamekianState()

class AndroidState(TransformationState):

    def __init__(self):
        self.constMaxLife = 10
        self.life = self.constMaxLife
        self.mana = 20
        self.attackPower = 10
        self.levelRequired = 0

    def getEvolve(self):
        return CyborgState()


# ------------------------------ Transformation ------------------------------ #

# ---------------------------------- SAIYEN ---------------------------------- #
class SuperSaiyenState(TransformationState):

    def __init__(self):
        self.constMaxLife = 30
        self.life = self.constMaxLife
        self.mana = 60
        self.attackPower = 10
        self.levelRequired = 1

    def getEvolve(self):
        return GorilleGeantState()

class GorilleGeantState(TransformationState):

    def __init__(self):
        self.constMaxLife = 30
        self.life = self.constMaxLife
        self.mana = 60
        self.attackPower = 10
        self.levelRequired = 2

    def getEvolve(self):
        print("pas devolution")


# --------------------------------- NAMEKIANS -------------------------------- #
class SuperNamekianState(TransformationState):

    def __init__(self):
        self.constMaxLife = 40
        self.life = self.constMaxLife
        self.mana = 20
        self.attackPower = 20
        self.levelRequired = 1

    def getEvolve(self):
        return AssimilationState()

class AssimilationState(TransformationState):

    def __init__(self):
        self.constMaxLife = 45
        self.life = self.constMaxLife
        self.mana = 30
        self.attackPower = 25
        self.levelRequired = 2

    def getEvolve(self):
        print("pas devolve")


# ---------------------------------- ANDROID --------------------------------- #
class CyborgState(TransformationState):

    def __init__(self):
        self.constMaxLife = 20
        self.life = self.constMaxLife
        self.mana = 25
        self.attackPower = 15
        self.levelRequired = 1

    def getEvolve(self):
        return PotaraFusionState()



class PotaraFusionState(TransformationState):

    def __init__(self):
        self.constMaxLife = 40
        self.life = self.constMaxLife
        self.mana = 30
        self.attackPower = 20
        self.levelRequired = 2

    def getEvolve(self):
        print("pas devolution")
