from PyPDF2 import PdfWriter, PdfReader


class MergePDFs:

    def __init__(self, forms_list):
        output_pdf = PdfWriter()

        for form in forms_list:
            pdf_template = PdfReader(open(f'pliki/forms/{form}.pdf', 'rb'))
            overlay_pdf = PdfReader(open(f'temp/{form}_overlay_PDF.pdf', 'rb'))

            def repeat():
                for i in range(5):
                    try:
                        template_page = pdf_template.pages[i]
                        template_page.merge_page(overlay_pdf.pages[i])
                        output_pdf.add_page(template_page)
                    except IndexError:
                        pass

            if form == 'detain':
                for _ in range(3):
                    repeat()
            else:
                repeat()

        output_pdf.write(open(f'pliki/scalone.pdf', "wb"))
