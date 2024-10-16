from src.Characteres import WarriorFactory, Race, SuperSaiyen, GorilleGeant
from src.TrainingMode import Training


if __name__ == "__main__":
    saiyen = WarriorFactory().createWarrior(Race.SAIYEN)
    print(saiyen.life)
    print(saiyen.allTransformation)
    roomOfTime = Training.getInstance()
    roomOfTime.trainCharactere(saiyen, 1)
    print(saiyen.unlockTransformation)
    roomOfTime.trainCharactere(saiyen, 1)
    print(saiyen.unlockTransformation)