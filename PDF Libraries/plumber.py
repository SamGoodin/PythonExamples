# Below line changes the program's encoding to desired encoding
# -*- coding: utf-8 -*-
import pdfplumber
import sys

pdf = pdfplumber.open('hw1 2021.pdf')

print(pdf.pages[0].extract_text())

for page in pdf.pages:
    # Plumber is able to decode all chars, but there is an issue
    # with outputting special chars to console. To solve, we encode 
    # print value with utf-8. Not sure if writing to file is the same
    try:
        print(page.extract_text().encode('utf-8'))
    except Exception as e:
        print(e)
        
for page in pdf.pages:
    try:
        # This approach replaces non-ascii chars with a ?
        # From here we can remove the ?
        # decode removes b'~' and \n
        print(page.extract_text().encode('ascii', 'replace').decode())
    except Exception as e:
        print(e)
        
for page in pdf.pages:
    try:
        # Words is a dictionary
        words = page.extract_words()
        for word in words:
            pass
            # Encode every word in ascii, ignoring non-ascii chars
            # Decode to remove string literals b'', returns string
            # W/O decode returns bytes
            #print(word['text'].encode('ascii', 'ignore').decode())
    except Exception as e:
        print(e)
        

"""
pdf = pdfplumber.open('Capstone projects.pdf')
pages = pdf.pages
first_page = pages[0]

# page.extract_text() returns the entire page as a string
# -therefore, string manipulation is possible
#print(first_page.extract_text())


for page in pages:
    print(page.extract_text())

# extracts text, removes spaces from text, puts remaining words into a list
print(first_page.extract_text().split(" "))

# extracts text, removes \n chars
print(repr(first_page.extract_text().replace('\n', '')))
"""
    
pdf.close()