from src.Characteres import WarriorFactory, Race, SuperSaiyen, GorilleGeant
from src.TrainingMode import Training

# Personaliser mon personnage

# choisir entre entrainement et combat

# -- combat
# choisir entre 
# - utiliser un objet 
#   -- btn --
#   retour
#   par attaque
# - Attaquer 
#   -- btn --
#   retour
#   par attaque
# - Transformation
#   -- bouton -- 
#   - retour
#   - par transformation 

character = None
roomOfTime = Training.getInstance()

def creationCharacterMenu():
    global character
    print("Choisis ton perso :")
    i = input("\n1: Saiyen \n2: Android \n3: Namekian")
    match i:
        case "1":
            character = WarriorFactory().createWarrior(Race.SAIYEN)
        case "2":
            character = WarriorFactory().createWarrior(Race.ANDROID)
        case "3":
            character = WarriorFactory().createWarrior(Race.NAMEKIANS)
    character.showStats()

def mainMenu():
    global character

    i = input("\n1: Entrainement \n 2 : Combat")
    match i:
        case "1":
            roomOfTime.trainCharactere(character, 1)
        case "2":
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