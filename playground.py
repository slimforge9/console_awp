from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader

overlay_pdf_file_name = 'temp/overlay_PDF.pdf'
pdf_template_file_name = 'forms/detain.pdf'
result_pdf_file_name = 'output/final_PDF.pdf'

# This section creates a PDF containing the information you want to enter in the fields
# on your base PDF.
pdf = FPDF(format='letter', unit='pt')
pdf.add_page()
pdf_style = ''
pdf.add_font('DejaVu', fname='DejaVuSansCondensed.ttf')
pdf.set_font('DejaVu', size=11)

def transform_p(p_no):
    add = " "
    napis = f"{p_no[0] + add + add + p_no[1] + add + add + add}"
    napis += f"{p_no[2] + add + add + p_no[3] + add + add + p_no[4]}"
    napis += f"{add + add + p_no[5] + add + add + p_no[6] + add + add}"
    napis += f"{p_no[7] + add + add + add + p_no[8] + add + add + p_no[9]}"
    napis += f"{add + add + p_no[10]}"
    return napis

tekst = 'Osoba poszukiwana Nakazem doprowadzenia sygn. akt IIIK 124/22 przez SR Gliwice celem odbycia kary 2 lat i 5 miesięcy pozbawienia wolności'

pdf.set_xy(230, 472)
pdf.cell(50, 15, txt='Adam', border=0)
pdf.set_xy(270, 472)
pdf.cell(50, 15, txt='Sobierajski', border=0)
pdf.set_xy(302, 240)
pdf.cell(50, 15, txt='2', border=0)
pdf.set_xy(315, 240)
pdf.cell(50, 15, txt='1', border=0)

pdf.set_xy(44, 60)
pdf.multi_cell(483, 12, txt=' '*9+tekst+' ' + 'f'*40, border=1)
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



