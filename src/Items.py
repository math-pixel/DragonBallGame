
# ---------- Items Protocol
class ItemProtocol():

    def __init__(self):
        pass

    def use(self):
        pass

# ---------- Items 
class DragonBall(ItemProtocol):

    def __init__(self):
        pass

    def use(self, warrior):
        print(f" *** warrior {warrior.stateCombat} a utiliser une senzu beam***")
        warrior.stateTransformation.mana += 50
        warrior.removeItem(warrior.items.index(self))

class SenzuBeam(ItemProtocol):

    def __init__(self):
        pass

    def use(self, warrior):
        print(f" *** warrior {warrior.stateCombat} a utiliser une senzu beam***")
        warrior.stateTransformation.life = warrior.stateTransformation.constMaxLife
        warrior.removeItem(warrior.items.index(self))

class Antidote(ItemProtocol):

    def __init__(self):
        pass

    def use(self, warrior):
        warrior.stateTransformation.life += 10
        warrior.removeItem(warrior.items.index(self))
        print(f" *** warrior {warrior.stateCombat} a utiliser un antidote ***")