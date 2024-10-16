from src.Characteres import WarriorFactory, Race
from src.TrainingMode import Training


if __name__ == "__main__":
    saiyen = WarriorFactory().createWarrior(Race.SAIYEN)
    print(saiyen.__dict__)
    roomOfTime = Training.getInstance()
    roomOfTime.trainCharactere(saiyen, 1)
    print(saiyen.__dict__)