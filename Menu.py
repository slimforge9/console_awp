from ChoseForms import ChoseForms
from sys import exit
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# colores text in terminal
colorama_init()


class Menu:

    @staticmethod
    def menu():
        option = input(f"{Fore.RED}(wpisz cyfrę z Menu i naciśnij ENTER)\n{Style.RESET_ALL}"
                       f"{Fore.GREEN}Wybierz opcję: {Style.RESET_ALL}1. Kreator, 2. O aplikacji 3. Wyjście\n"
                       f"{Fore.GREEN}Wybieram opcję: {Style.RESET_ALL}")

        if option == '1':
            cos = ChoseForms()
            chosen_forms = cos.chose_forms()
            return chosen_forms
        else:
            print("Do widzenia!")
            exit()
