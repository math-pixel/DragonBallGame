import os

class FORM:
    # Static method to display a form and execute the corresponding function based on the user's choice
    @staticmethod
    def display(title: str, choices: list[str], functions: list[callable]):
        """
        Displays a form with a title and choices, and executes the function corresponding to the user's choice.

        :param title: The title to display at the top of the form.
        :param choices: A list of strings representing the available choices.
        :param functions: A list of functions to execute corresponding to the choices.
        """

        # Print the title
        print(title)
        
        # Print the choices
        for index, choice in enumerate(choices, start=1):
            print(f"{index}: {choice}")
        
        # Get the user's input
        try:
            user_input = int(input("\nChoisis une option: "))
            
            # Check if the input is within the range of available choices
            if 1 <= user_input <= len(choices):
                # Execute the corresponding function
                return functions[user_input - 1]()
            else:
                print("Choix invalide, veuillez réessayer.")
                FORM.display(title, choices, functions)  # Re-display the form if the input is invalid
                
        except ValueError:
            print("Veuillez entrer un numéro valide.")
            FORM.display(title, choices, functions)  # Re-display the form in case of invalid input

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

# Example usage:

# def go_back():
#     print("Retour en arrière...")

# def simple_attack():
#     print("Exécution de l'attaque simple...")

# def special_attack():
#     print("Exécution de l'attaque spéciale...")

# Using the static class FORM to display choices and handle the logic
# FORM.display(
#     "Choisis le type de ton attaque :", 
#     ["<-- Back", "simple Attaquer", "Attack Special"], 
#     [go_back, simple_attack, special_attack]
# )


from enum import Enum

# Enum pour différents niveaux de log et leurs couleurs
class LogLevel(Enum):
    INFO = "\x1b[32m"    # Vert pour les messages d'information
    WARNING = "\x1b[33m" # Jaune pour les avertissements
    ERROR = "\x1b[31m"   # Rouge pour les erreurs
    DEBUG = "\x1b[34m"   # Bleu pour le débogage
    CRITICAL = "\x1b[35m" # Magenta pour les messages critiques

# Fonction de log
def log(message: str, level: LogLevel):
    # Appliquer la couleur en fonction du niveau de log
    print(f"{level.value}{message}\x1b[0m")  # Le \x1b[0m réinitialise la couleur après le message

