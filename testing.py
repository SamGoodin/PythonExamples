from glob import glob

#Prints out all pdf files within this directory
print(glob('*.pdf'))

import pdfplumber

pdf = pdfplumber.open('Capstone projects.pdf')
#page = pdf.pages[0]
for page in pdf.pages:
    text = page.extract_text()
    print(text)
pdf.close()