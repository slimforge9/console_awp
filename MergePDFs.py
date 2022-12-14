from PyPDF2 import PdfFileWriter, PdfFileReader

class MergePDFs:

    def __init__(self, forms_list):
        output_pdf = PdfFileWriter()

        for form in forms_list:
            pdf_template = PdfFileReader(open(f'forms/{form}.pdf', 'rb'))
            overlay_pdf = PdfFileReader(open(f'temp/{form}_overlay_PDF.pdf', 'rb'))

            for i in range(3):
                try:
                    template_page = pdf_template.getPage(i)
                    template_page.mergePage(overlay_pdf.getPage(i))
                    output_pdf.addPage(template_page)
                except IndexError:
                    pass

        output_pdf.write(open(f'merged.pdf', "wb"))

