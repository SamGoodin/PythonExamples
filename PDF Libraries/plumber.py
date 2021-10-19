import pdfplumber


pdf = pdfplumber.open('Capstone projects.pdf')
pages = pdf.pages
first_page = pages[0]

# page.extract_text() returns the entire page as a string
# -therefore, string manipulation is possible
#print(first_page.extract_text())

"""
for page in pages:
    print(page.extract_text())
"""

# extracts text, removes spaces from text, puts remaining words into a list
print(first_page.extract_text().split(" "))

# extracts text, removes \n chars
print(repr(first_page.extract_text().replace('\n', '')))
    
pdf.close()