from input_reading import read_input_pdf
from text_processing import text_extraction
from text_processing import text_processing
from output_manupulation import output_calculation
from output_manupulation import save_output


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

def run():
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
