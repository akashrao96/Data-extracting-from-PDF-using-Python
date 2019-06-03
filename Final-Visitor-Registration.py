import PyPDF2
import csv
import re
pdfFileObj = open('/home/akashrao96/Downloads/Final-Visitor-Registration.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pages=pdfReader.numPages
print(pages)
s=" "
f = open('Final-Visitor-Registration.csv', 'w')
for page in range(pages):
	pageObj = pdfReader.getPage(page)
	s=pageObj.extractText()
	email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",s)
	print(email)
	writer=csv.writer(f)
	writer.writerow(email)
f.close()
pdfFileObj.close()
