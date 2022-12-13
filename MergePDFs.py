from PyPDF2 import PdfFileWriter, PdfFileReader
from CoordinatesDB import fields_db
from FillForm import FillForm
from GetData import GetData
from Menu import Menu


class MergePDFs:

    def __init__(self, forms_list):
        collected_data = GetData().fill_fields()
        data = collected_data.copy()
        for form in forms_list:
            obj = FillForm(form, fields_db, data)
            obj.set_form_positions()


    def num_pages(form_name):
        return len(fields_db[form_name].keys())

    # def merge_files(self, forms_list):
    #     # self.template_filepaths()
    #
    #     for form in forms_list:
    #
    #         # open template
    #         pdf_template = PdfFileReader(open(f'forms/{form}.pdf', 'rb'))
    #
    #         # open overlay
    #         overlay_pdf = PdfFileReader(open(f'temp/{form}_overlay_PDF.pdf', 'rb'))
    #
    #         for page in range(MergePDFs.num_pages(form)):
    #             # get page from the template
    #             template_page = pdf_template.getPage(page)
    #             template_page.mergePage(overlay_pdf.getPage(page))
    #
    #             output_pdf = PdfFileWriter()
    #             output_pdf.addPage(template_page)
    #             output_pdf.write(open(f'output/{form}.pdf', "wb"))

        # print(self.template_paths)
        # print(self.temp_paths)
        # print(self.out_paths)

    # print(num_pages('warrant'))
#
dupa = MergePDFs(Menu().menu())
# dupa.merge_files()



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
