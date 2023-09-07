'''import aspose.pdf as pdf'''
""""import PyPDF2
import camelot""" 
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io
import glob
from datetime import datetime

def main():
   readPdf_To_STPT()
   #readPdf_To_PTST()
""""
def readPdf():
    pdf_file = open('Dicionario_livre_santome_portugues_Livlu.pdf')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    pdf = page_content.encode('utf-8')
    print(pdf)"""
def readPdf_To_STPT():
    fp = open("Dicionario_livre_santome_portugues_Livlu.pdf", 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)
    count = 0
    for page in pages:
        count += 1
        if count >= 23 and count <= 98:
            interpreter.process_page(page)
            data =  retstr.getvalue()
            #write the data in the text file to improve the pdf read. Have some erros!
            with open('SantoPT.txt', 'a', encoding='utf-8') as f:
                f.write(data)

def readPdf_To_PTST():
    fp = open("Dicionario_livre_santome_portugues_Livlu.pdf", 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)
    count = 0
    for page in pages:
        count += 1
        if (count >= 101 and count <= 172):
            interpreter.process_page(page)
            data =  retstr.getvalue()
            #write the data in the text file to improve the pdf read. Have some erros!
            with open('PTSanto.txt', 'a', encoding='utf-8') as f:
                f.write(data)

if __name__ == '__main__':
    main()