from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter,TextConverter,XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
import PyPDF2
import re

def convert(case,fname, pages=None):
    if not pages: pagenums = set();
    else:         pagenums = set(pages);      
    manager = PDFResourceManager()
    codec = 'utf-8'
    caching = True

    if case == 'text' :
        output = io.StringIO()
        converter = TextConverter(manager, output, codec=codec, laparams=LAParams())    

    interpreter = PDFPageInterpreter(manager, converter)  
    infile = open(fname, 'rb')

    for page in PDFPage.get_pages(infile, pagenums,caching=caching, check_extractable=False):
        interpreter.process_page(page)

    convertedPDF = output.getvalue()  

    infile.close(); converter.close(); output.close()
    return convertedPDF

#//////////// main ///////////////////////
filePDF  = '崙子段1588-2地號謄本.pdf'     # input
fileHTML = 'myHTML.html'   # output
fileTXT  = 'myTXT.txt'     # output
file = open(filePDF, 'rb')
fileReader = PyPDF2.PdfFileReader(file)

pages = [i for i in range(fileReader.numPages)]
convertedPDF = convert('text', filePDF, pages=pages)
fileConverted = open(fileTXT,"w",encoding="utf-8")

fileConverted.write(convertedPDF)
fileConverted.close()
file.close()

切割關鍵字列表 = re.findall("（[0-9][0-9][0-9][0-9]）", convertedPDF)
關鍵字索引列表 = []

for 切割關鍵字 in 切割關鍵字列表 :
    關鍵字索引列表.append(convertedPDF.find(切割關鍵字));
關鍵字索引列表.append(convertedPDF.find("〈 本謄本列㊞完畢 〉"));

start = 0
end = 1
土地所有權列表 = []
for 關鍵字索引 in range(len(關鍵字索引列表)-1):
    print(convertedPDF[關鍵字索引列表[start]:關鍵字索引列表[end]])
    土地所有權列表.append(convertedPDF[關鍵字索引列表[start]:關鍵字索引列表[end]])
    start = start + 1
    end = end + 1

















