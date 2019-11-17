#!/usr/bin/python

from PyPDF2 import PdfFileWriter, PdfFileReader

with open("in.pdf", "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()
    
    numPages = input1.getNumPages()
    print("document has " + str(numPages) + " pages")
    
    for i in range(numPages):
        page = input1.getPage(i)
        print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        page.trimBox.lowerLeft = (0, 0)
        page.trimBox.upperRight = (595, 842)
        page.cropBox.lowerLeft = (15, 45)
        page.cropBox.upperRight = (580, 842)
        output.addPage(page)
    
    with open("out.pdf", "wb") as out_f:
        output.write(out_f)
