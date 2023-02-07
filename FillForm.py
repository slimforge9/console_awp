from fpdf import FPDF
from PyPDF2 import PdfWriter, PdfReader


class FillForm:

    def __init__(self, form_name, coord_db, collected_data):

        self.line = None  # container for generator result
        self.form_name = form_name
        self.coord_db = coord_db
        self.collected_data = collected_data
        self.overlay_pdf_file_name = f'temp/{self.form_name}_overlay_PDF.pdf'
        self.pdf_template_file_name = f'pliki/forms/{self.form_name}.pdf'
        self.result_pdf_file_name = f'pliki/output/{self.form_name}.pdf'

        # prepare PDF file
        self.pdf = FPDF(format='letter', unit='pt')
        self.pdf.add_font('DejaVu', fname='fonts/DejaVuSansCondensed.ttf')  # UTF-8 font - accepts polish signs
        self.pdf.set_font('DejaVu', size=11)

    # TRANSFORM p_no with spaces to fill detain form
    def transform_p(self, p_no):
        add = " "
        pesel = f"{p_no[0] + add + add + p_no[1] + add + add + add}"
        pesel += f"{p_no[2] + add + add + p_no[3] + add + add + p_no[4]}"
        pesel += f"{add + add + p_no[5] + add + add + p_no[6] + add + add}"
        pesel += f"{p_no[7] + add + add + add + p_no[8] + add + add + p_no[9]}"
        pesel += f"{add + add + p_no[10]}"
        return pesel

    def num_pages(self):
        return len(list(self.coord_db[self.form_name].keys()))

    def generate_form_positions(self, page):
        # CREATES GENERATOR
        # iteration trough pages in form\
        for k, v in self.coord_db[self.form_name][f'page{page}'].items():
            yield k, v

    def set_form_positions(self):
        # iterate trough pages
        for pages in range(self.num_pages()):

            # create a generator for each field position and resets it after every page
            self.line = iter(self.generate_form_positions(pages))
            self.pdf.add_page()

            # this loop place values in right coords, there's alot of "elif" because of customization of every form
            # which has different place/cell/multi_cell logic
            while True:
                try:
                    # gets key, value_xy from generator
                    key, value_xy = next(self.line)

                except StopIteration:
                    break

                # DETAIN FORM
                # detain_hour
                if self.form_name == 'detain' and key == 'hd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['detain_time'][0], border=0)

                elif self.form_name == 'detain' and key == 'hj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['detain_time'][1], border=0)

                elif self.form_name == 'detain' and key == 'hmd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['detain_time'][3], border=0)

                elif self.form_name == 'detain' and key == 'hmj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['detain_time'][4], border=0)

                # detain_date
                # day
                elif self.form_name == 'detain' and key == 'ddd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['detain_date'][0], border=0)

                elif self.form_name == 'detain' and key == 'ddj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['detain_date'][1], border=0)

                # month
                elif self.form_name == 'detain' and key == 'dmd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['detain_date'][3], border=0)

                elif self.form_name == 'detain' and key == 'dmj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['detain_date'][4], border=0)

                # year
                elif self.form_name == 'detain' and key == 'dyt':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['detain_date'][6], border=0)

                elif self.form_name == 'detain' and key == 'dys':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['detain_date'][7], border=0)

                elif self.form_name == 'detain' and key == 'dyd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['detain_date'][8], border=0)

                elif self.form_name == 'detain' and key == 'dyj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['detain_date'][9], border=0)

                # doc_time
                elif self.form_name == 'detain' and key == 'doc_hd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_time'][0], border=0)

                elif self.form_name == 'detain' and key == 'doc_hj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_time'][1], border=0)

                elif self.form_name == 'detain' and key == 'doc_hmd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_time'][3], border=0)

                elif self.form_name == 'detain' and key == 'doc_hmj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_time'][4], border=0)

                # doc_date
                # day
                elif self.form_name == 'detain' and key == 'doc_ddd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][0], border=0)

                elif self.form_name == 'detain' and key == 'doc_ddj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][1], border=0)

                # month
                elif self.form_name == 'detain' and key == 'doc_dmd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][3], border=0)

                elif self.form_name == 'detain' and key == 'doc_dmj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][4], border=0)

                # year
                elif self.form_name == 'detain' and key == 'doc_dyt':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][6], border=0)

                elif self.form_name == 'detain' and key == 'doc_dys':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][7], border=0)

                elif self.form_name == 'detain' and key == 'doc_dyd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][8], border=0)

                elif self.form_name == 'detain' and key == 'doc_dyj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][9], border=0)

                elif self.form_name == 'detain' and key == 'detain_basis':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(483, 12, txt=' '*35 + self.collected_data[key], border=0)

                elif self.form_name == 'detain' and key == 'rights':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(483, 12, txt=' '*11 + self.collected_data[key], border=0)

                # end_time_hour
                elif self.form_name == 'detain' and key == 'ehd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_time'][0], border=0)

                elif self.form_name == 'detain' and key == 'ehj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_time'][1], border=0)

                elif self.form_name == 'detain' and key == 'emd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_time'][3], border=0)

                elif self.form_name == 'detain' and key == 'emj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_time'][4], border=0)

                # end_doc_date
                # day
                elif self.form_name == 'detain' and key == 'eddd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][0], border=0)

                elif self.form_name == 'detain' and key == 'eddj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][1], border=0)

                # month
                elif self.form_name == 'detain' and key == 'edmd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][3], border=0)

                elif self.form_name == 'detain' and key == 'edmj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][4], border=0)

                # year
                elif self.form_name == 'detain' and key == 'edyt':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][6], border=0)

                elif self.form_name == 'detain' and key == 'edys':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][7], border=0)

                elif self.form_name == 'detain' and key == 'edyd':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][8], border=0)

                elif self.form_name == 'detain' and key == 'edyj':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(490, 10, txt=self.collected_data['doc_date'][9], border=0)

                ######################

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
                    self.pdf.set_xy((value_xy[0]+(len(self.collected_data['doc_city'])*4)), value_xy[1])
                    self.pdf.cell(50, 15, txt=self.collected_data[key], border=0)

                elif self.form_name == 'rej' and key == 'doc_date':
                    self.pdf.set_xy((value_xy[0]+(len(self.collected_data['doc_city'])*7)), value_xy[1])
                    self.pdf.cell(50, 15, txt=self.collected_data[key], border=0)

                elif self.form_name == 'rej' and key == 'victim':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(280, 10, txt=self.collected_data[key], border=0)

                elif self.form_name == 'rej' and key == 'subject':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.multi_cell(280, 10, txt=self.collected_data[key], border=0)

                elif self.form_name == 'detain' and key == 'p_no':
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.cell(50, 15, txt=self.transform_p(self.collected_data[key]), border=0)

                elif self.form_name == 'identity' and key == 'pic':
                    try:
                        filepath = f'pliki/images/{self.collected_data["name"]} {self.collected_data["surname"]}.jpg'
                        with self.pdf.rotation(270):
                            self.pdf.image(filepath, x=470, y=100, w=200, h=150)
                    except FileNotFoundError:
                        print("Nie dodałeś zdjęcia w folderze 'pliki/images/imie nazwisko.jpg")

                elif key[-1] != '2' and key[-1] != '3':
                    # sets x,y with text from dictionary by key
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.cell(50, 15, txt=self.collected_data[key], border=0)

                else:
                    self.pdf.set_xy(value_xy[0], value_xy[1])
                    self.pdf.cell(50, 15, txt=self.collected_data[key[0:-1]], border=0)

            # add blank page to manage two-side print in real life printer (in forms that have only one page)
            # if self.form_name == '79':
            #     self.pdf.add_page()
            if self.form_name == 'identity':
                self.pdf.add_page()
            if self.form_name == 'warrant':
                self.pdf.add_page()

        # save to file with all pages
        self.pdf.output(self.overlay_pdf_file_name)

        # rest
        pdf_template = PdfReader(open(self.pdf_template_file_name, 'rb'))

        # Open your overlay PDF that was created earlier
        overlay_pdf = PdfReader(open(self.overlay_pdf_file_name, 'rb'))

        # Write the result to a new PDF file
        output_pdf = PdfWriter()

        for i in range(self.num_pages()):
            # Get the first page from the template
            template_page = pdf_template.pages[i]
            # Merge the overlay page onto the template page
            template_page.merge_page(overlay_pdf.pages[i])
            output_pdf.add_page(template_page)

        output_pdf.write(open(self.result_pdf_file_name, "wb"))
