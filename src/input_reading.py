from PyPDF2 import PdfReader


def read_input_pdf(fileName):
    pdf_file_name = 'resume_pdf_files/Arslan_Arif_AI_2021.pdf'
    pdfReader = PdfReader(pdf_file_name) # Read file
    return pdfReader

