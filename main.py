from FillFields import FillFields
from FillForm import FillForm
from FormsFieldsDB import fields_db

# collected data
collected_data = FillFields().fill_fields()

# creates overlay_pdf of chosen form -> 'warrant'
form = FillForm('warrant', fields_db, collected_data)
form.set_form_positions()

