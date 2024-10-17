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
                return Saiyen([PunchAttack()], [PunchCharged()], [SenzuBeam()], life=20, mana=10)
            case Race.ANDROID:
                return Android([PunchAttack()], [PunchCharged()], [SenzuBeam()], life=10, mana=50)
            case Race.NAMEKIANS:
                return Namekians([PunchAttack()], [PunchCharged()], [SenzuBeam()], life=15, mana=30)

class WarriorProtocol():

    def __init__(self, race, attacks, attackSpe, items, life = 10, mana = 10):
        self.constMaxLife:int = life
        self.life:int = life
        self.mana:int = mana
        self.race:Race = race
        self.attack:list[AttackStandard] = attacks
        self.attackSpe:list[AttackSpe] = attackSpe
        self.state:StateWarrior = BasicState()
        self.items:list[ItemProtocol] = items
        self.level:int = 1
        self.xp:int = 0
        self.allTransformation:WarriorProtocol = []
        self.unlockTransformation:WarriorProtocol = []
        self.description:str = ""

    def checkLevelUp(self):
        if self.xp >= 10 and self.xp < 20:
            if self.level == 1:
                self.unlockTransformation.append(self.allTransformation[0])
                print(f"yay a new transformation : {self.allTransformation[0].__name__}")
            self.level = 2
        elif self.xp >= 20 and self.xp < 30:
            if self.level == 2:
                self.unlockTransformation.append(self.allTransformation[1])
                print(f"yay a new transformation : {self.allTransformation[1].__name__}")

            self.level = 3
        # elif self.xp >= 30 and self.xp < 40:
        #     if self.level == 2:
        #         self.unlockTransformation.append(self.allTransformation[2])
        #     self.level = 3

    def showStats(self):
        print(self.life, self.mana, self.race, self.attack, self.attackSpe, self.state, self.items, self.level, self.xp, self.allTransformation, self.unlockTransformation, self.description)

    def isAlive(self):
        return self.life > 0
    
    def upgradeWarrior(self,xpEarn, life = None, mana = None, attack = None, attackSpe = None, transformation = None):
        
        print("------ Result of Training ------")

        self.xp += xpEarn
        self.checkLevelUp()
        
        if(life != None):
            self.life += life
            print(f"life + {life}")

        if(mana != None):
            self.mana += mana
            print(f"mana + {mana}")

        if(attack != None):
            self.attack.append(attack)
            print(f"yay a new attack : {attack}")

        if(attackSpe != None):
            self.attackSpe.append(attackSpe)
            print(f"yay a new special attack : {attackSpe}")

        if(transformation != None):
            pass

        print("--------------------------------")

    def applyStateEffect(self):
        # applique leffet au guerrier
        self.state.applyEffect(self)

    def changeState(self, newState:StateWarrior):
        self.state = newState

    def addItem(self, item:ItemProtocol):
        self.items.append(item)

    def removeItem(self, itemIndex:int):
        self.items.pop(itemIndex)

class Saiyen(WarriorProtocol):

    def __init__(self, attacks, attackSpe, items, life=10, mana=10):
        super().__init__(Race.SAIYEN, attacks, attackSpe, items, life, mana)
        self.allTransformation = [SuperSaiyen, GorilleGeant]

class Android(WarriorProtocol):

    def __init__(self, attacks, attackSpe, items, life=10, mana=10):
        super().__init__(Race.ANDROID, attacks, attackSpe, items, life, mana)
        self.allTransformation = [Cyborg, PotaraFusion]


class Namekians(WarriorProtocol):

    def __init__(self, attacks, attackSpe, items, life=10, mana=10):
        super().__init__(Race.NAMEKIANS, attacks, attackSpe, items, life, mana)
        self.allTransformation = [SuperNamekian, Assimilation]


# ------------------------------ Transformation ------------------------------ #

# ---------------------------------- SAIYEN ---------------------------------- #
class SuperSaiyen(Saiyen):

    def __init__(self, saiyen:Saiyen):
        self.saiyen = saiyen
        self.life = self.saiyen.life + 20
        self.description = f"+ {self.life} vie | "

class GorilleGeant(Saiyen):

    def __init__(self, saiyen:Saiyen):
        self.saiyen = saiyen
        self.life = self.saiyen.life + 15
        self.description = f"+ {self.life} vie | "


# --------------------------------- NAMEKIANS -------------------------------- #
class SuperNamekian(Namekians):

    def __init__(self, namekian:Namekians):
        self.namekian = namekian
        self.life = self.namekian.life + 20
        self.description = f"+ {self.life} vie | "

class Assimilation(Namekians):

    def __init__(self, namekian:Namekians):
        self.namekian = namekian
        self.life = self.namekian.life + 20
        self.description = f"+ {self.life} vie | "


# ---------------------------------- ANDROID --------------------------------- #
class Cyborg(Android):

    def __init__(self, android:Android):
        self.android = android
        self.life = self.android.life + 20
        self.description = f"+ {self.life} vie | "



class PotaraFusion(Android):

    def __init__(self, android:Android):
        self.android = android
        self.life = self.android.life + 30
        self.description = f"+ {self.life} vie | "
