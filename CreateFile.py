import fpdf
from PyPDF2 import PdfFileWriter, PdfFileReader


from FillFields import FillFields
from FieldInput import FieldInput


class CreateFile:

    def __init__(self, collected_data, chosen_forms, form, ):

        # dictionary with collected data
        self.start = FillFields().fill_fields()

        # chosen forms
        self.chosen_forms = FieldInput.chosen_forms






