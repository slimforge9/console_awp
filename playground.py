from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader


overlay_pdf_file_name = 'temp/overlay_PDF.pdf'
pdf_template_file_name = 'forms/79.pdf'
result_pdf_file_name = 'output/final_PDF.pdf'

# This section creates a PDF containing the information you want to enter in the fields
# on your base PDF.
pdf = FPDF(format='letter', unit='pt')
pdf.add_page()
pdf_style = ''
pdf.add_font('DejaVu', fname='DejaVuSansCondensed.ttf')
pdf.set_font('DejaVu', size=11)

pdf.set_xy(90, 163)
pdf.cell(50, 15, txt='Kuneguda', border=0)
pdf.set_xy((90+(len('Kuneguda')*7)), 163)
pdf.cell(50, 15, txt='Macierewicz', border=0)
pdf.output(overlay_pdf_file_name)


# Take the PDF you created above and overlay it on your template PDF
# Open your template PDF
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