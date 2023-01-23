from Menu import Menu
from FormsDB import FormsDB

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# colores text in terminal
colorama_init()

class FieldInput:

    # returns chosen forms
    chosen_forms = Menu().menu()
    if 'identity' in chosen_forms:
        print(f"[Potw. Tożsamości] {Fore.RED}Dodaj zdjęcie osoby w formacie 'Imię Nazwisko.jpg' w folderze pliki/images.\n"
              f"Nazwa z imieniem i nazwiskiem musi odpowiadać tym samym danym, które wpiszesz jako imię i nazwisko osoby"
              f"\nponiżej: {Style.RESET_ALL}(wielkość liter ma odpowiadać tym wpisanym inaczej będzie błąd)")

    # needed fields list in chosen forms
    form = FormsDB()
    needed_data = form.get_fields()

    # create list of fields in chosen forms without repetition
    flattened_fields_list = form.fields_list(chosen_forms, needed_data)

    def give_list(self):
        return FieldInput.flattened_fields_list

    def get_forms_list(self):
        return self.chosen_forms
