from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader
from FieldInput import FieldInput
import main

# database of fields coordinates to fill in chosen forms
db = {'detain': {'page0':
                     {'name': [1, 2],
                      'surname': [10, 10]},
                 'page1':
                     {'p_end_h': [20, 20],
                      'p_end_date': [30, 40]}
                 },
      'warrant': {'page0':
                      {'name': [130, 280],
                       'surname': [200, 280],
                       'dad_name': [360, 280],
                       'p_no': [360, 315]}}}


overlay_pdf_file_name = 'temp/overlay_PDF.pdf'
pdf_template_file_name = 'forms/warrant.pdf'
result_pdf_file_name = 'output/warrant.pdf'

# prepare PDF file
pdf = FPDF(format='letter', unit='pt')
pdf_style = ''
pdf.add_font('DejaVu', fname='fonts/DejaVuSansCondensed.ttf')
pdf.set_font('DejaVu', size=11)


def num_pages(form_name):
    return len(db[form_name].keys())


def get_form_positions(form_name):
    # iteration trough pages in form
    for i in range(num_pages(form_name)):
        # iteration trough items in pages form
        page = i
        # print(f"strona{i}")
        for k, v in db[form_name][f'page{i}'].items():
            yield page, k, v


# collected data for function under
collected_data = main.start


def set_form_positions(form_name, collected_data_dict):

    # set
    pages_amount = num_pages(form_name)

    # iterate trough pages
    for pages in range(pages_amount):

        # create a generator for each field position
        line = iter(get_form_positions(form_name))
        pdf.add_page()

        while True:
            try:
                # gets key, value_xy
                page, key, value_xy = next(line)

            except StopIteration:
                break

            # sets x,y with text from dictionary by key
            pdf.set_xy(value_xy[0], value_xy[1])
            pdf.cell(50, 15, txt=collected_data_dict[key], border=0)

    # save to file
    pdf.output(overlay_pdf_file_name)


# data needed for function under
chosen_forms = FieldInput.chosen_forms


def manage_form_with_data(forms_list):
    for form in forms_list:
        set_form_positions(f'{form}', collected_data)


##### TEST
manage_form_with_data(chosen_forms)

##### REST TO HANDLE
# pdf.output(overlay_pdf_file_name)

pdf_template = PdfFileReader(open(pdf_template_file_name, 'rb'))
# Get the first page from the template
template_page = pdf_template.getPage(0)
# Open your overlay PDF that was created earlier
overlay_pdf = PdfFileReader(open(overlay_pdf_file_name, 'rb'))
# Merge the overlay page onto the template page
template_page.mergePage(overlay_pdf.getPage(0))
# Write the result to a new PDF file
output_pdf = PdfFileWriter()
output_pdf.addPage(template_page)
output_pdf.write(open(result_pdf_file_name, "wb"))
