from PyPDF2 import PdfReader


def read_input_pdf(file_name):
    pdf_file_name = file_name
    pdfReader = PdfReader(pdf_file_name) # Read file
    return pdfReader

