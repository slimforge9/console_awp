from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader


class FillForm:

    def __init__(self, form_name, coord_db, collected_data):

        self.line = None  # container for generator result
        self.form_name = form_name
        self.coord_db = coord_db
        self.collected_data = collected_data
        self.overlay_pdf_file_name = f'temp/{self.form_name}_overlay_PDF.pdf'
        self.pdf_template_file_name = f'forms/{self.form_name}.pdf'
        self.result_pdf_file_name = f'output/{self.form_name}.pdf'

        # prepare PDF file
        self.pdf = FPDF(format='letter', unit='pt')
        self.pdf.add_font('DejaVu', fname='fonts/DejaVuSansCondensed.ttf')  # UTF-8 font - accepts polish signs
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

            # this loop place values in right coords, there's alot of "elif" because of customization of every form
            # which has different place/cell/multi_cell logic
            while True:
                try:
                    # gets key, value_xy from generator
                    key, value_xy = next(self.line)

                except StopIteration:
                    break

                if key == '79_basis':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data[key], border=0)

                elif key == 'act_description':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(280, 10, txt=self.collected_data[key], border=0)

                elif self.form_name == '79' and key == 'doc_date':
                    self.pdf.set_xy((value_xy[0]+(len(self.collected_data['doc_city'])*7)), value_xy[1])
                    self.pdf.cell(50, 15, txt=self.collected_data[key], border=0)

                elif self.form_name == 'warrant' and key == 'doc_date':
                    self.pdf.set_xy((value_xy[0]+(len(self.collected_data['doc_city'])*7)), value_xy[1])
                    self.pdf.cell(50, 15, txt=self.collected_data[key], border=0)

                elif self.form_name == 'warrant' and key == 'doc_time':
                    self.pdf.set_xy((value_xy[0]+(len(self.collected_data['doc_date'])*7)), value_xy[1])
                    self.pdf.cell(50, 15, txt=self.collected_data[key], border=0)

                elif self.form_name == 'rej' and key == 'doc_date':
                    self.pdf.set_xy((value_xy[0]+(len(self.collected_data['doc_city'])*7)), value_xy[1])
                    self.pdf.cell(50, 15, txt=self.collected_data[key], border=0)

                elif key[-1] != '2':
                    # sets x,y with text from dictionary by key
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.cell(50, 15, txt=self.collected_data[key], border=0)

                else:
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.cell(50, 15, txt=self.collected_data[key[0:-1]], border=0)

            # add blank page to manage two-side print in real life printer (in forms that have only one page)
            if self.form_name == '79':
                self.pdf.add_page()
            if self.form_name == 'warrant':
                self.pdf.add_page()

        # save to file with all pages
        self.pdf.output(self.overlay_pdf_file_name)

        # rest
        pdf_template = PdfFileReader(open(self.pdf_template_file_name, 'rb'))
        # Get the first page from the template
        template_page = pdf_template.getPage(0)
        # Open your overlay PDF that was created earlier
        overlay_pdf = PdfFileReader(open(self.overlay_pdf_file_name, 'rb'))
        # Merge the overlay page onto the template page
        template_page.mergePage(overlay_pdf.getPage(0))
        # Write the result to a new PDF file
        output_pdf = PdfFileWriter()
        output_pdf.addPage(template_page)
        output_pdf.write(open(self.result_pdf_file_name, "wb"))


