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
        self.startTraining(levelOfTraining, BaseTraining())

    def startTraining(self, level, trainerBase):
        # TODO GAME

        trainer = trainerBase
        match level:
            case 1:
                trainer = XpTraining(trainer)                
                # self.warriorToTrain.upgradeWarrior(xpEarn= xpTraining.getXp())
            case 2:
                trainer = LifeTraining(trainer)                
                # self.warriorToTrain.upgradeWarrior(xpEarn= xpTraining.getXp())
            case 3:
                trainer = ManaTraining(trainer)                
                # self.warriorToTrain.upgradeWarrior(xpEarn= xpTraining.getXp())
            case _:
                pass
        self.warriorToTrain.upgradeWarrior(xpEarn= trainer.getXp(), life = trainer.getLife(), mana = trainer.getMana(), attack = trainer.getAttack(), attackSpe = trainer.getAttackSpe())




# interface
class TrainingLevel:
    def getXp(self): pass
    def getLife(self): pass
    def getMana(self): pass
    def getAttack(self): pass
    def getAttackSpe(self): pass

class BaseTraining(TrainingLevel):
    
    def __init__(self):
        self.xpEarn = 1
        self.life = 2
        self.mana = 5
        self.attack = None
        self.attackSpe = None

    def getXp(self): return self.xpEarn
    def getLife(self): return self.life
    def getMana(self): return self.mana
    def getAttack(self): return self.attack
    def getAttackSpe(self): return self.attackSpe


class TrainingLevelDecorator(TrainingLevel):
    
    def __init__(self, trainer: TrainingLevel):
        self.trainer = trainer

    def getXp(self): return self.trainer.getXp()
    def getLife(self): return self.trainer.getLife()
    def getMana(self): return self.trainer.getMana()
    def getAttack(self): return self.trainer.getAttack()
    def getAttackSpe(self): return self.trainer.getAttackSpe()

class XpTraining(TrainingLevelDecorator):

    def getXp(self): return self.trainer.getXp() + 10


class LifeTraining(TrainingLevelDecorator):

    def getLife(self): return self.trainer.getLife() + 5

class ManaTraining(TrainingLevelDecorator):

    def getMana(self): return self.trainer.getMana() + 3 