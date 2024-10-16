from src.Characteres import WarriorProtocol, WarriorFactory

class Training():

    instance = None

    def __init__(self):
        self.warriorToTrain = None

    def getInstance(): 
        if(Training.instance == None):
            Training.instance = Training()
        return Training.instance

    def trainCharactere(self, warrior:WarriorProtocol, levelOfTraining):
        self.warriorToTrain = warrior
        self.startTraining(levelOfTraining)

    def upgradeCharactere(self, life = None, mana = None, attack = None, attackSpe = None, transformation = None):
        if(life != None):
            self.warriorToTrain.life += life

        if(mana != None):
            self.warriorToTrain.mana += mana

        if(attack != None):
            self.warriorToTrain.attack.append(attack)

        if(attackSpe != None):
            self.warriorToTrain.attackSpe.append(attackSpe)

        if(transformation != None):
            pass

    def startTraining(self, level):
        # TODO GAME
        self.upgradeCharactere(life=2, mana=1)