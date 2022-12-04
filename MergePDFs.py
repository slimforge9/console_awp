from Menu import Menu
from CoordinatesDB import fields_db


class MergePDFs:

    def __init__(self, forms_list):
        self.forms_list = forms_list
        self.paths = []

    def forms_filepath(self):
        for form in self.forms_list:
            path = f'temp/{form}_overlay_PDF.pdf'
            self.paths.append(path)

        return self.paths  # returns [list] of paths to forms_overlay_pdfs

    def num_pages(form_name):
        return len(fields_db[form_name].keys())


    print(num_pages('warrant'))



dupa = MergePDFs(Menu().menu())
print(dupa.forms_filepath())



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
