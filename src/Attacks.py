# from src.Characteres import WarriorProtocol

# --------- Attack General Protocol
class AttackProtocol:
    
    def __init__(self):
        self.consumeMana = 3
        self.dammage = 5

    def attack(self, warriorAttacker,  warriorDefender):
        self.giveDammage(warriorAttacker,  warriorDefender)
        self.giveEffect(warriorAttacker,  warriorDefender)

    def giveDammage(self, warriorAttacker,  warriorDefender):
        warriorAttacker.mana -= self.consumeMana
        warriorDefender.life -= self.dammage

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

if __name__ == "__main__":
    punch = PunchAttack()
    chargedPunch = PunchCharged()
    print(punch.dammage, " - ", chargedPunch.dammage)
