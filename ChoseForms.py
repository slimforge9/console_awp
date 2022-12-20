from sys import exit
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# colores text in terminal
colorama_init()


class ChoseForms:
    # Creates list of forms needed to be created,

    def __init__(self):
        self.forms_list = ['detain', 'warrant', '79', 'rej']
        self.translator = {'detain': ' - Protokół zatrzymania osoby',
                           'warrant': ' - Nakaz przyjęcia do PDOZ',
                           '79': ' - Notatka z doprowadzenia na podstawie art 79kkw',
                           'rej': ' - Notatka rejestracyjna do kradzieży do wykroczeń KSIP'}

    def chose_forms(self):
        # Add or remove form to fill
        chosen_forms = []
        clear = "\n" * 100
        print(clear)
        print(f"{Fore.GREEN}\nLista dokumentów, które zostaną sporządzone po wybraniu opcji Dalej:{Style.RESET_ALL}")
        print(f"{Fore.BLUE} - brak (wybierz cyfrą odpowiedni dokument i naciśnij ENTER){Style.RESET_ALL}")


        while True:
            option = input(f"{Fore.GREEN}\nWybierz dokument do wypełnienia (wpisz cyfrę z Menu i naciśnij ENTER):{Style.RESET_ALL}"
                           f"{Fore.YELLOW}\nJeśli dokument jest na liście, wybierz go ponownie aby usunąć go z listy{Style.RESET_ALL}\n\n"
                           " 1. Protokół zatrzymania osoby\n 2. Nakaz przyjęcia do PDOZ\n "
                           "3. Notatka z doprowadzenia art 79kkw\n 4. Notatka Rejestracyjna do wykroczeń KSIP\n"
                           f"{Fore.RED} 5. Dalej lub zakończ (jeśli brak jest dokumentów na liście)\n{Style.RESET_ALL}"
                           f"{Fore.GREEN}\nWybieram opcję: {Style.RESET_ALL}")

            if option == '1':
                if self.forms_list[0] not in chosen_forms:
                    chosen_forms.append(self.forms_list[0])
                elif self.forms_list[0] in chosen_forms:
                    chosen_forms.remove(self.forms_list[0])
            elif option == '2':
                if self.forms_list[1] not in chosen_forms:
                    chosen_forms.append(self.forms_list[1])
                elif self.forms_list[1] in chosen_forms:
                    chosen_forms.remove(self.forms_list[1])
            elif option == '3':
                if self.forms_list[2] not in chosen_forms:
                    chosen_forms.append(self.forms_list[2])
                elif self.forms_list[2] in chosen_forms:
                    chosen_forms.remove(self.forms_list[2])
            elif option == '4':
                if self.forms_list[3] not in chosen_forms:
                    chosen_forms.append(self.forms_list[3])
                elif self.forms_list[3] in chosen_forms:
                    chosen_forms.remove(self.forms_list[3])
            else:
                if chosen_forms:
                    break
                else:
                    print(f"{Fore.RED}Nie wybrałeś żadnych dokumentów. Do widzenia! :){Style.RESET_ALL}")
                    exit()
            print(clear)
            if chosen_forms:
                print(f"{Fore.GREEN}Lista dokumentów, które zostaną sporządzone po wybraniu opcji Dalej:{Style.RESET_ALL}")
                for form in chosen_forms:
                    print(f"{Fore.BLUE}{self.translator[form]}{Style.RESET_ALL}")
            else:
                print(
                    f"{Fore.GREEN}\nLista dokumentów, które zostaną sporządzone po wybraniu opcji Dalej:{Style.RESET_ALL}")
                print(f"{Fore.BLUE} - brak (wybierz cyfrą odpowiedni dokument i naciśnij ENTER){Style.RESET_ALL}")
        return chosen_forms

# print(f'{Fore.RED}BŁĄD!{Style.RESET_ALL})


