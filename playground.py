from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader

overlay_pdf_file_name = 'temp/overlay_PDF.pdf'
pdf_template_file_name = 'forms/rej.pdf'
result_pdf_file_name = 'output/final_PDF.pdf'

# This section creates a PDF containing the information you want to enter in the fields
# on your base PDF.
pdf = FPDF(format='letter', unit='pt')
pdf.add_page()
pdf_style = ''
pdf.add_font('DejaVu', fname='DejaVuSansCondensed.ttf')
pdf.set_font('DejaVu', size=11)

pdf.set_xy(255, 704)
pdf.cell(50, 15, txt='Bartłomiej', border=0)
pdf.set_xy(255, 681)
pdf.cell(50, 15, txt='Krupiński', border=0)
pdf.set_xy(255, 263)
pdf.multi_cell(280, 10, txt='Gliwice', border=1)
pdf.output(overlay_pdf_file_name)


# Take the PDF you created above and overlay it on your template PDF
# Open your template PDF
pdf_template = PdfFileReader(open(pdf_template_file_name, 'rb'))
# Get the first page from the template
template_page = pdf_template.getPage(1)
# Open your overlay PDF that was created earlier
overlay_pdf = PdfFileReader(open(overlay_pdf_file_name, 'rb'))
# Merge the overlay page onto the template page
template_page.mergePage(overlay_pdf.getPage(0))
# Write the result to a new PDF file
output_pdf = PdfFileWriter()
output_pdf.addPage(template_page)
output_pdf.write(open(result_pdf_file_name, "wb"))



# # creates 2 pages form if there's 1 page form
# overlay_pdf_file_name = 'temp/overlay_PDF.pdf'
# pdf_template_file_name = 'forms/warrant.pdf'
# result_pdf_file_name = 'output/2_pages_war.pdf'
# pdf_pusty = PdfFileReader(open('forms/blank.pdf', 'rb'))
# pusty = pdf_pusty.getPage(0)
# pdf_79 = PdfFileReader(open('forms/warrant.pdf', 'rb'))
# siedemdziewiec = pdf_79.getPage(0)
# pdf_template = PdfFileWriter(open(pdf_template_file_name, 'rb'))
# pdf_template.addPage(siedemdziewiec)
# pdf_template.addPage(pusty)
# pdf_template.write(open(result_pdf_file_name, "wb"))


# from PIL import Image
#
# basewidth = 300
# img = Image.open('somepic.jpg')
# wpercent = (basewidth/float(img.size[0]))
# hsize = int((float(img.size[1])*float(wpercent)))
# img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
# img.save('somepic.jpg')

