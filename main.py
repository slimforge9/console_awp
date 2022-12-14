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
except:
    print('Nie obsluzyles wszystkich inputow')

MergePDFs(chosen_forms)

print(collected_data)
print(chosen_forms)
