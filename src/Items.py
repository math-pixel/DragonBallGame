
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
        print(f" *** warrior {warrior.race} a utiliser une senzu beam***")
        warrior.mana += 50
        warrior.removeItem(warrior.items.index(self))

class SenzuBeam(ItemProtocol):

    def __init__(self):
        pass

    def use(self, warrior):
        print(f" *** warrior {warrior.race} a utiliser une senzu beam***")
        warrior.life = warrior.constMaxLife
        warrior.removeItem(warrior.items.index(self))

class Antidote(ItemProtocol):

    def __init__(self):
        pass

    def use(self, warrior):
        warrior.life += 10
        warrior.removeItem(warrior.items.index(self))
        print(f" *** warrior {warrior.race} a utiliser un antidote ***")