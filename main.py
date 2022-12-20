from FillFields import FillFields
from FieldInput import FieldInput
from CoordinatesDB import fields_db
from MergePDFs import MergePDFs

from FillForm import FillForm

# chosen forms from menu
chosen_forms = FieldInput.chosen_forms

# collected data in chosen forms
collected_data = FillFields().fill_fields()

try:
    # fill forms
    for form in chosen_forms:
        FillForm(f'{form}', fields_db, collected_data).set_form_positions()
except KeyError as ke:
    print(f'BŁĄD: W slowniku koordynatow masz {ke} czego nie wpisales w liście formsDB')

MergePDFs(chosen_forms)

print(collected_data)
print(chosen_forms)

# import datetime
#
# x = datetime.datetime.now()
#     date = time.strftime("%d.%m.%Y"+' .r')
# print(x.strftime("%d.%m.%Y"))
# print(x.strftime("%H:%M"))
# ZWRACA STRINGI WIEC MOZNA SLICE'OWAC ;)