import PyPDF2
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combined.pdf")

''' run with the desired pdfs inside the same files as the main.py
    then it will be merged and outputted as a file titles combined.pdf '''
