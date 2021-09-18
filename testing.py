class Animal:
    descriptions = {}

    def __init__(self, name, colors, sounds):
        self.name = name
        self.descriptions['color'] = colors
        self.descriptions['sound'] = sounds

    def setAttrTest(self, functionName, stats):
        # setattr(object, function name, function

        def functionToRun(self):
            print(stats['desc'])

        setattr(Animal, functionName, functionToRun)


cat = Animal("cat", ['blue'], ['meow'])
cat.setAttrTest("talk", {
    'damage': 23,
    'penetration': 1.2,
    'heal': 5,
    'cost': 15,
    'desc': "a fiery magical attack"
})
cat.talk()


from glob import glob

#Prints out all pdf files within this directory
print(glob('*.pdf'))

import pdfplumber

pdf = pdfplumber.open('Capstone projects.pdf')
#page = pdf.pages[0]
for page in pdf.pages:
    text = page.extract_text()
    #print(text)
pdf.close()
