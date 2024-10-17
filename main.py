from src.Characteres import WarriorFactory, Race
from src.TrainingMode import Training
from src.Combat import Arene
from src.tools import *

# Personaliser mon personnage

# choisir entre entrainement et combat


character = None
roomOfTime = Training.getInstance()
arene = None

def creationCharacterMenu():
    global character
    character = FORM.display("Choisis ton perso :", ["Saiyen","Android","Namekian"], [lambda: WarriorFactory().createWarrior(Race.SAIYEN), lambda : WarriorFactory().createWarrior(Race.ANDROID), lambda : WarriorFactory().createWarrior(Race.NAMEKIANS)])
    character.showStats()

def mainMenu():
    global character
    global arene

    i = input("\n1: Entrainement \n 2 : Combat")
    match i:
        case "1":
            roomOfTime.trainCharactere(character, 1)
            mainMenu()
        case "2":
            arene = Arene(character)
            arene.playerTurnFight()





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