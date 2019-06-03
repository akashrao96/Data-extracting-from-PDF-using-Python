import PyPDF2
import re
pdfFileObj = open('student.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
text = ""
for page_number in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(page_number)
    text+=pageObj.extractText()

studentList = re.compile(r"\([0-9][0-9]\)").split(text)

outfile = open("studentData.csv","w")
for student in studentList:
    mob = re.findall(r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",student)
    num_removed_student = student
    for num in mob:
        num_removed_student = student.replace(num,"")
    email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",num_removed_student)
    print(mob,email)
    outfile.write(",".join(email)+","+",".join(mob)+"\n")
pdfFileObj.close()
