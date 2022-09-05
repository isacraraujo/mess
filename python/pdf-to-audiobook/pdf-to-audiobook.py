# pip install pyttsx3
# pip install PyPDF2

import pyttsx3, PyPDF2
import os

book      = open('.\file.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages     = pdfReader.numPages
print(pages)

speaker   = pyttsx3.init()
page      = pdfReader.getPage(6)
text      = page.extractText()

speaker.say(text)
speaker.runAndWait()