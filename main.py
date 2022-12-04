from GetData import GetData
from FillForm import FillForm
from CoordinatesDB import fields_db

# starts menu, collecting needed data -> person data, forms list
collected_data = GetData().fill_fields()

# creates overlay_pdf of chosen form -> 'warrant'
form = FillForm('warrant', fields_db, collected_data)
form.set_form_positions()

