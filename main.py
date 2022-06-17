# Import required libraries
from PyPDF2 import PdfReader
import textract
import re
import string
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline


# Create dictionary with industrial and system engineering key terms by area
terms = {'CV':['opencv', 'tensorflow', 
               'image classification', 
               'image segmentation', 
               'object detection'],      

        'NLP':['nlp, ''transformer', 
              'encoder decoder', 
              'bert', 'text analysis',
              'sentiment analysis',
              'chatbot', 'pytorch', 
              'NLTK', 'sequence model', 
              'text mining'],

        'Tradition ML':['python','matplotlib',
                        'scikit learn', 'regression', 
                        'numpy', 'pandas'],

        'Other skills': ['python', 'git', 'docker']
        }


def read_input_pdf(fileName):
    pdf_file_name = 'resume_pdf_files/Arslan_Arif_AI_2021.pdf'
    pdfReader = PdfReader(pdf_file_name) # Read file
    return pdfReader


def average_calculator(opencv, nlp, trad_ml, others, terms):
    cv_avg = (opencv/len(terms['CV']))*100
    nlp_avg = (nlp/ len(terms['NLP']))*100
    trad_ml_avg = (trad_ml/len(terms['Tradition ML']))*100
    others_avg = (others/len(terms['Other skills']))*100
    return cv_avg, nlp_avg, trad_ml_avg, others_avg


def text_extraction(pdfReader):
    num_pages = len(pdfReader.pages) # Get total number of pages
    # print("total number of pages in pdf file: ", num_pages)
    count = 0 # Initialize a count for the number of pages
    text = "" # Initialize a text empty string variable
    # Extract text from every page on the file and concatenate in the text variable 
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
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


def output_calculation(text):
    # Initializie score counters for each area
    opencv = 0
    nlp = 0
    trad_ml = 0
    others = 0

    # Obtain the scores for each area
    for area in terms.keys():
            
        if area == 'CV':
            for word in terms[area]:
                if word in text:
                    opencv +=1            

        elif area == 'NLP':
            for word in terms[area]:
                if word in text:
                    nlp +=1
            
        elif area == 'Tradition ML':
            for word in terms[area]:
                if word in text:
                    trad_ml +=1        
            
        else:        
            for word in terms[area]:
                if word in text:
                    others +=1        
    cv_avg, nlp_avg, trad_ml_avg, others_avg = average_calculator(opencv, nlp, trad_ml, others, terms)
    return [cv_avg, nlp_avg, trad_ml_avg, others_avg]


def save_output(avg_res):
    print("terms.keys(): ",terms.keys())
    summary = pd.DataFrame(avg_res,index=terms.keys(),columns=['score']).sort_values(by='score',ascending=False)    
    summary.to_csv("results/resume_summary.csv")
    print("summary.index", summary.index)
    # Create pie chart visualization
    pie = plt.figure(figsize=(10,10))
    plt.pie(np.array(avg_res)/100, labels=['CV', 'NLP', 'Tradition ML', 'Other skills'], explode = (0.1,0,0,0), autopct='%1.0f%%',shadow=True,startangle=90)
    plt.title('Machine Learning Engineering Candidate - Resume Decomposition by Areas')
    plt.axis('equal')
    plt.show()
    # Save pie chart as a .png file
    pie.savefig('results/resume_screening_results.png')

    

# step1
fileName = "resume_pdf_files/Arslan_Arif_AI_2021.pdf"
pdfReader = read_input_pdf(fileName)

# step2
text = text_extraction(pdfReader)

# step3
text = text_processing(text)

# step4

avg_res_list = output_calculation(text)

# step5

save_output(avg_res_list)
