import fpdf
from PyPDF2 import PdfFileWriter, PdfFileReader

# from FillFields import FillFields
# from FieldInput import FieldInput
#
# # dictionary with collected data
# start = FillFields().fill_fields()
#
# # chosen forms
# chosen_forms = FieldInput.chosen_forms

class FileHandler:

    def __init__(self):
        pass

    def place_data(self, chosen_forms, collected_data, database):
        # print(list.index('curly'))

        for form in chosen_forms:
            in_page1 = (next(item for item in database[form]))  # CZARNA MAGIA
            # print(key)
            print(database[form][in_page1])
            # for field_name, value in enumerate(database[form][key]):
            #     # print(database[form][key][value])
            #     print(field_name)
            #     print(value)

            # for field_name, value in enumerate(database[form][key]):
            #     print(value)
            #     print(database[form][key][index])
                # print((value[0], value[1]))  # pdf.set_xy
                # print(f'{database[form][key].keys()}')  # pdf.cell(50, 15, txt=, border=0)


    def save_file(self):
        pass

cos = FileHandler()
cos.place_data(chosen_forms2, data, db)
#
#
# # setting file names
# overlay_pdf_file_name = 'overlay_PDF.pdf'
# pdf_template_file_name = 'forms/detain.pdf'
# result_pdf_file_name = 'final_PDF.pdf'
#
# # This section creates a PDF containing the information you want to enter in the fields
# # on your base PDF.
# pdf = fpdf.FPDF(format='letter', unit='pt')
# pdf.add_page()
# pdf_style = ''
# pdf.add_font('DejaVu', fname='DejaVuSansCondensed.ttf')
# pdf.set_font('DejaVu', size=11)
#
# # creating dictionary of positions in pdf-forms
# p_detain_dict_pos = {'name_surname_pos': [70, 87],
#                      'detention_time_pos': [380, 84],
#                      'detention_date_pos': [450, 84]
#                      }
#
# # iterating trough dictionary to set cells positions with input stored in memory
# for index, value in enumerate(p_detain_dict_pos.values()):
#     pdf.set_xy(value[0], value[1])
#     pdf.cell(50, 15, txt=f'{cell_addresses[index]}', border=0)
#
#
#
# pdf.output(overlay_pdf_file_name)
# pdf.close()
#
#
# # Take the PDF you created above and overlay it on your template PDF
# # Open your template PDF
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
