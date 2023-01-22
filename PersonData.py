from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# colores text in terminal
colorama_init()
class PersonData:

    def __init__(self):
        self.name = input(f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Imię osoby której dotyczy protokół: ')
        self.surname = input(f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Nazwisko: ')
        self.p_no = input(f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} PESEL: ')
        self.address = input(f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Miejsce zamieszkania {Fore.CYAN}(np: Warszawa, ul. Kręta 6/2): {Style.RESET_ALL}')

        def convert_birth_from_p_no(b_date):
            if b_date[2] == '2' or b_date[2] == '3':
                temp = str(int(b_date[2] + b_date[3]) - 20)
                if len(temp) == 1:
                    temp = f'0{temp}'
                return f'{b_date[4]}{b_date[5]}.{temp}.20{b_date[0]}{b_date[1]} r.'
            else:
                return f'{b_date[4]}{b_date[5]}.{b_date[2]}{b_date[3]}.19{b_date[0]}{b_date[1]} r.'

        self.person_data = {'name': self.name,
                            'surname': self.surname,
                            'p_no': self.p_no,
                            'address': self.address,
                            'birth_date': convert_birth_from_p_no(self.p_no)
                            }

    def get_data(self):
        return self.person_data
