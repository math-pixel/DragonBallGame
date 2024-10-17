from src.Characteres import Warrior, WarriorFactory

class Training():

    instance = None

    def __init__(self):
        self.warriorToTrain = None

    def getInstance(): 
        if(Training.instance == None):
            Training.instance = Training()
        return Training.instance

    def trainCharactere(self, warrior:Warrior, levelOfTraining):
        self.warriorToTrain = warrior
        self.startTraining(levelOfTraining)


    def startTraining(self, level):
        # TODO GAME
        self.warriorToTrain.upgradeWarrior(xpEarn = 10, life=2, mana=1)