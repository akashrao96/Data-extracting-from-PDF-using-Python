import PyPDF2
import re
import csv
pdfFileObj = open('/home/akashrao96/Downloads/P-Member.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
s = ""
for page_number in range(30,175):
    pageObj = pdfReader.getPage(page_number)
    s+=pageObj.extractText()

Lists = re.compile(r"\([0-9][0-9][0-9][0-9][0-9]\)").split(s)

f= open("P-Member.csv","w")
for List in Lists:
	mob = re.findall(r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",List)
	email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",List)
	print(mob,email)
	writer=csv.writer(f)
	writer.writerow(email)
	writer.writerow(mob)
	    
pdfFileObj.close()
