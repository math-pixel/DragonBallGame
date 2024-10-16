from src.Characteres import WarriorFactory, Race, SuperSaiyen, GorilleGeant
from src.TrainingMode import Training


if __name__ == "__main__":
    saiyen = WarriorFactory().createWarrior(Race.SAIYEN)
    print(saiyen.life)
    roomOfTime = Training.getInstance()
    roomOfTime.trainCharactere(saiyen, 1)
    print(saiyen.life)
    saiyen = SuperSaiyen(saiyen)
    print(saiyen.life)
    saiyen = GorilleGeant(saiyen)
    print(saiyen.life)