import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from requirements_dict import *


def average_calculator(opencv, nlp, trad_ml, others, terms):
    cv_avg = (opencv/len(terms['CV']))*100
    nlp_avg = (nlp/ len(terms['NLP']))*100
    trad_ml_avg = (trad_ml/len(terms['Tradition ML']))*100
    others_avg = (others/len(terms['Other skills']))*100
    return cv_avg, nlp_avg, trad_ml_avg, others_avg


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
