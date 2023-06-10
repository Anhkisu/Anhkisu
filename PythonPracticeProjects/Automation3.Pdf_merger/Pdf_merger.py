#Import Library
import pypdf
import sys
import os

merger = pypdf.PdfMerger()
#Loop to select files in OS
#Check if File is PDF then merger
for file in os.listdir(r'C:\Users\TowfNguyenx\Desktop\TheRoot\Work\Coding\Anhkisu\PythonPracticeProjects\Automation3.Pdf_merger'):
    if file.endswith('.pdf'):
        merger.append(file)
    merger.write("COMBINEDPdf.pdf")

