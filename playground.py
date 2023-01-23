from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image

overlay_pdf_file_name = 'temp/overlay_PDF.pdf'
pdf_template_file_name = 'pliki/forms/identity.pdf'
result_pdf_file_name = 'output/final_PDF.pdf'

# This section creates a PDF containing the information you want to enter in the fields
# on your base PDF.
pdf = FPDF(format='letter', unit='pt')
pdf.add_page()
pdf_style = ''
pdf.add_font('DejaVu', fname='DejaVuSansCondensed.ttf')
pdf.set_font('DejaVu', size=11)


filepath = f'pliki/images/F F.jpg'
with pdf.rotation(270):
    pdf.image(filepath, x=40, y=-305, w=200, h=150)


pdf.set_xy(350, 375)
pdf.cell(50, 15, txt='11111111111', border=0)
pdf.set_xy(145, 509)
pdf.cell(50, 15, txt='Piotr', border=0)
pdf.set_xy(330, 550)
pdf.cell(50, 15, txt='Adalajewska', border=0)
pdf.set_xy(120, 665)
pdf.cell(50, 15, txt='Sobierajska', border=0)








pdf.set_xy(440, 600)
pdf.multi_cell(483, 12, txt=' '*9+' ' + 'f'*40, border=1)
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



# creates 2 pages form if there's 1 page form

# result_pdf_file_name = 'output/2_pages_identity.pdf'
# pdf_pusty = PdfFileReader(open('forms2/blank.pdf', 'rb'))
# pusty = pdf_pusty.getPage(0)
# pdf_79 = PdfFileReader(open('forms2/identity.pdf', 'rb'))
# siedemdziewiec = pdf_79.getPage(0)
# pdf_template = PdfFileWriter(open(pdf_template_file_name, 'rb'))
# pdf_template.addPage(siedemdziewiec)
# pdf_template.addPage(pusty)
# pdf_template.write(open(result_pdf_file_name, "wb"))


# from PIL import Image
#
# basewidth = 300
# img = Image.open(f'somepic.jpg')
# wpercent = (basewidth/float(img.size[0]))
# hsize = int((float(img.size[1])*float(wpercent)))
# img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
# img.save('somepic.jpg')



# Założyć profil w którym:
# stopien, imie nazwisko policjanta
# Miejscowosc dokumentu
# nr legitymacji sluzbowej
# kierownik jednostki


#                 elif self.form_name == 'identity':
#                     try:
#                         filepath = f'pliki/images/{self.collected_data["name"]} {self.collected_data["surname"]}.jpg'
#                         with self.pdf.rotation(270):
#                             self.pdf.image(filepath, x=40, y=-305, w=200, h=150)
#                     except FileNotFoundError:
#                         print("Nie dodałeś zdjęcia w folderze 'pliki/images/imie nazwisko.jpg")

#
#                 # DODALEM GLIWICE JAKO DOMYSLNE MIASTO
#                 elif field == 'doc_city':
#                     all_data['doc_city'] = 'Gliwice'
#                     print(all_data['doc_city'])