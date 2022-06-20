import re
import string


def text_extraction(pdf_reader):
    num_pages = len(pdf_reader.pages) # Get total number of pages
    # print("total number of pages in pdf file: ", num_pages)
    count = 0 # Initialize a count for the number of pages
    text = "" # Initialize a text empty string variable
    # Extract text from every page on the file and concatenate in the text variable 
    while count < num_pages:
        pageObj = pdf_reader.getPage(count)
        count +=1
        text += pageObj.extractText()
    return text


def text_processing(text):
    text = text.lower() # Convert all strings to lowercase
    print("text in lower case\n\n", text)
    text = re.sub(r'\d+','',text) # Remove numbers
    # print("text after removing the numbers ", text)
    text = text.translate(str.maketrans('','',string.punctuation)) # Remove punctuation
    # print("text after removing punctuation: ", text)
    return text
