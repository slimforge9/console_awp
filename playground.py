from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader


# database of fields coordinates to fill in chosen forms
db = {'detain': {'page0':
                      {'name': [0, 0],
                       'surname': [10, 10]},
                 'page1':
                      {'p_end_h': [20, 20],
                       'p_end_date': [30, 40]}
                 },
      'warrant': {'page0':
                      {'name': [1, 1],
                       'surname': [2, 2]}}
      }


overlay_pdf_file_name = 'temp/overlay_PDF.pdf'
pdf_template_file_name = 'forms/warrant.pdf'
result_pdf_file_name = 'output/warrant.pdf'


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
        print(f"strona{i}")
        for k, v in db[form_name][f'page{i}'].items():
            yield page, k, v


def set_form_positions(form_name, collected_data_dict):
    line = iter(get_form_positions(form_name))
    while True:
        try:
            page, key, value_xy = next(line)
            print(page, key, value_xy)

        except StopIteration:
            break



set_form_positions('detain', 1)

#
#
#
# # pdf.set_xy(380, 84)
# # pdf.cell(50, 15, txt='dupa', border=0)
#
# pdf.output(overlay_pdf_file_name)
#
# pdf_template = PdfFileReader(open(pdf_template_file_name, 'rb'))
# # Get the first page from the template
# template_page = pdf_template.getPage(0)
# # Open your overlay PDF that was created earlier
# overlay_pdf = PdfFileReader(open(overlay_pdf_file_name, 'rb'))
# # Merge the overlay page onto the template page
# template_page.mergePage(overlay_pdf.getPage(0))
# # Write the result to a new PDF file
# output_pdf = PdfFileWriter()
# output_pdf.addPage(template_page)
# output_pdf.write(open(result_pdf_file_name, "wb"))