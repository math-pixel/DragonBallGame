class StateWarrior():
    def applyEffect(self):
        pass

class BasicState(StateWarrior):
    def applyEffect(self, warrior):
        pass

class PoisonedState(StateWarrior):
    
    def __init__(self, duration):
        self.duration = duration

    def applyEffect(self, warrior):
        if self.duration > 0:
            warrior.life -= 2  # Par exemple, 2 points de dégâts par tour
            print(f"{warrior.race} est empoisonné ! Il perd 2 points de vie.")
            self.duration -= 1
        if self.duration == 0:
            warrior.state = BasicState()

class ParalyzedState(StateWarrior):
    
    def __init__(self, duration=1):
        self.duration = duration

    def applyEffect(self, warrior):
        if self.duration > 0:
            print(f"{warrior.race} est paralysé et passe son tour.")
            self.duration -= 1
        if self.duration == 0:
            warrior.state = BasicState()