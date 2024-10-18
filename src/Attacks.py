from src.StateCharactere import *
from src.tools import *

# --------- Attack General Protocol
class AttackProtocol:
    
    def __init__(self):
        self.consumeMana = 3
        self.dammage = 5

    def attack(self, warriorAttacker,  warriorDefender):
        self.giveDammage(warriorAttacker,  warriorDefender)
        self.giveEffect(warriorAttacker,  warriorDefender)

    def giveDammage(self, warriorAttacker,  warriorDefender):
        warriorAttacker.stateTransformation.mana -= self.consumeMana
        warriorDefender.stateTransformation.life -= warriorAttacker.stateTransformation.attackPower + self.dammage

    def giveEffect(self, warriorAttacker,  warriorDefender):
        pass

# --------- All Attack Protocol
class AttackStandard(AttackProtocol):
    def __init__(self):
        super().__init__()

class AttackSpe(AttackProtocol):
    def __init__(self):
        super().__init__()

# --------- Attacks
class PunchAttack(AttackStandard):
    def __init__(self):
        super().__init__()
        self.consumeMana = 0
        self.dammage = 1


# --------- Attack Spe
class PunchCharged(AttackSpe):
    def __init__(self):
        super().__init__()
        self.consumeMana = 1
        self.dammage = 3

# TODO change name of class
class PoisonAttack(AttackStandard):
    def __init__(self):
        super().__init__()
        self.consumeMana = 2
        self.dammage = 1

    def giveEffect(self, warriorAttacker, warriorDefender):
        warriorDefender.changeState(PoisonedState(duration=3))
        log(f"{warriorDefender.race} est empoisonné !", LogLevel.INFO)

if __name__ == "__main__":
    punch = PunchAttack()
    chargedPunch = PunchCharged()
    print(punch.dammage, " - ", chargedPunch.dammage)
