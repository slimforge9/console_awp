from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader


class FillForm:

    def __init__(self, form_name, coord_db, collected_data):

        self.line = None
        self.form_name = form_name
        self.coord_db = coord_db
        self.collected_data = collected_data
        self.overlay_pdf_file_name = f'temp/{self.form_name}_overlay_PDF.pdf'
        self.pdf_template_file_name = f'forms/{self.form_name}.pdf'
        self.result_pdf_file_name = f'output/{self.form_name}.pdf'

        # prepare PDF file
        self.pdf = FPDF(format='letter', unit='pt')
        self.pdf.add_font('DejaVu', fname='fonts/DejaVuSansCondensed.ttf')
        self.pdf.set_font('DejaVu', size=11)

    def num_pages(self):
        return len(self.coord_db[self.form_name].keys())

    def generate_form_positions(self):
        # CREATES GENERATOR
        # iteration trough pages in form
        for i in range(self.num_pages()):
            # iteration trough items in pages form -> returns key and value
            for k, v in self.coord_db[self.form_name][f'page{i}'].items():
                yield k, v

    def set_form_positions(self):
        # iterate trough pages
        for pages in range(self.num_pages()):

            # create a generator for each field position and resets it after every page
            self.line = iter(self.generate_form_positions())
            self.pdf.add_page()

            while True:
                try:
                    # gets key, value_xy from generator
                    key, value_xy = next(self.line)

                except StopIteration:
                    break

                # sets x,y with text from dictionary by key
                self.pdf.set_xy(value_xy[0], value_xy[1])
                self.pdf.cell(50, 15, txt=self.collected_data[key], border=0)

        # save to file with all pages
        self.pdf.output(self.overlay_pdf_file_name)


