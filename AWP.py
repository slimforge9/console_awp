from FillFields import FillFields
from FieldInput import FieldInput
from CoordinatesDB import fields_db
from MergePDFs import MergePDFs
from FillForm import FillForm

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# colores text in terminal
colorama_init()

# chosen forms from menu
collected_data = FillFields().fill_fields()

# collected data in chosen forms
chosen_forms = FieldInput.chosen_forms


try:
    # fill forms
    for form in chosen_forms:
        FillForm(f'{form}', fields_db, collected_data).set_form_positions()
except KeyError as ke:
    print(f'{Fore.RED}BŁĄD!{Style.RESET_ALL}:W słowniku koordynatów masz {ke} czego nie wpisałeś w liście formsDB')
except TypeError:
    print("Do widzenia! - w mainie")


# merge chosen_forms into one pdf file
MergePDFs(chosen_forms)
print("Utworzono /pliki/scalone.pdf - otwórz i drukuj dwustronnie! :) ")

