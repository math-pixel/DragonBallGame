from src.Characteres import WarriorFactory, Race
from src.TrainingMode import Training
from src.Combat import Arena
from src.tools import *

# Personaliser mon personnage

# choisir entre entrainement et combat


character = None
bot = WarriorFactory().createWarrior(Race.SAIYEN)
roomOfTime = Training.getInstance()
arene = None

def creationCharacterMenu():
    global character
    character = FORM.display("Choisis ton perso :", ["Saiyen","Android","Namekian"], [lambda: WarriorFactory().createWarrior(Race.SAIYEN), lambda : WarriorFactory().createWarrior(Race.ANDROID), lambda : WarriorFactory().createWarrior(Race.NAMEKIANS)])

def mainMenu():
    global character
    global arene

    print("---------------------")
    print("----- Main Menu -----")
    print("---------------------")

    i = input("\n1: Entrainement \n2: Combat\n3: exit")
    match i:
        case "1":
            roomOfTime.trainCharactere(character, 1)
            mainMenu()
        case "2":
            arene = Arena(character, bot)
            mainMenu()
        case "3":
            pass





if __name__ == "__main__":
    # saiyen = WarriorFactory().createWarrior(Race.SAIYEN)
    # print(saiyen.life)
    # print(saiyen.allTransformation)
    # roomOfTime = Training.getInstance()
    # roomOfTime.trainCharactere(saiyen, 1)
    # print(saiyen.unlockTransformation)
    # roomOfTime.trainCharactere(saiyen, 1)
    # print(saiyen.unlockTransformation)
    creationCharacterMenu()
    mainMenu()