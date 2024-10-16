from src.Characteres import WarriorFactory, Race


if __name__ == "__main__":
    saiyen = WarriorFactory().createWarrior(Race.SAIYEN)
    android = WarriorFactory().createWarrior(Race.ANDROID)
    namek = WarriorFactory().createWarrior(Race.NAMEKIANS)
    print(saiyen, android, namek)