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
        self.life:int = life
        self.mana:int = mana
        self.race:Race = race
        self.attack:list[AttackStandard] = attacks
        self.attackSpe:list[AttackSpe] = attackSpe
        self.state:StateWarrior = BasicState()
        self.items:list[ItemProtocol] = items

class Saiyen(WarriorProtocol):

    def __init__(self, attacks, attackSpe, items, life=10, mana=10):
        super().__init__(Race.SAIYEN, attacks, attackSpe, items, life, mana)

class Android(WarriorProtocol):

    def __init__(self, attacks, attackSpe, items, life=10, mana=10):
        super().__init__(Race.ANDROID, attacks, attackSpe, items, life, mana)

class Namekians(WarriorProtocol):

    def __init__(self, attacks, attackSpe, items, life=10, mana=10):
        super().__init__(Race.NAMEKIANS, attacks, attackSpe, items, life, mana)

