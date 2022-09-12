#pip install PyPDF2
import PyPDF2

pdfFileObj = open(r"C:\file.pdf", "rb")
pdfReader  = PyPDF2.PdfFileReader(pdfFileObj)
print("Total Pages: ",pdfReader.numPages)

textObj    = pdfReader.getPage(0)
print("\n",textObj.extractText())
pdfFileObj.close()