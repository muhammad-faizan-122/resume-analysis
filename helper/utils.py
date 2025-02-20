from PyPDF2 import PdfReader
import re
import string
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yaml


def load_yml_cfgs(path):
    """
    load the resume configs
    """
    try:
        with open(path) as resume_file:
            resume_file = yaml.safe_load(resume_file)
            return resume_file
    except Exception as e:
        raise ValueError("Failed to Load resume configurations.")


def extract_text(resume_path):
    """
    Extracts text from each page of a PDF document.

    Args:
        pdf_reader (PdfReader): A PDF reader object containing the PDF document.

    Returns:
        str: The extracted text from all pages concatenated.
    """
    try:
        pdf_reader = PdfReader(resume_path)
        total_pages = len(pdf_reader.pages)
        page_num = 0
        page_texts = ""
        while page_num < total_pages:
            pageObj = pdf_reader.pages[page_num]
            page_num += 1
            page_texts += pageObj.extract_text()
        print("text extraction completed...")
        return page_texts

    except Exception as e:
        raise ValueError(f"Failed to extract Resume text due to {e}")


def preprocess(text):
    """
    Performs text processing operations on input text.

    Args:
        text (str): The input text to be processed.

    Returns:
        str: The processed text with lowercase letters and removed numbers and punctuation.
    """
    if not text:
        return text
    text_without_nums = re.sub(r"\d+", "", text.lower())  # Remove numbers
    text_without_punc = text_without_nums.translate(
        str.maketrans("", "", string.punctuation)
    )
    return text_without_punc


def count_field_keywords(tech_fields):
    """
    Count the number of keywords for each technical field in the keywords dictionary.

    Args:
        tech_fields (dict): Dictionary containing technical fields and their keywords.

    Returns:
        dict: A dictionary containing technical fields as keys and their respective keyword counts as values.
    """
    return {tech_field: len(keywords) for tech_field, keywords in tech_fields.items()}


def calculate_output_averages(
    cv_counts, nlp_counts, trad_ml_counts, others_counts, resume_keywords
):
    """
    Calculate the average score for each skill area.

    Calculates the average scores for different skill areas (e.g., CV, NLP, Traditional ML,
    Other skills) based on the provided scores and the total number of keywords for each area.

    Args:
        cv_counts (int): Count of CV-related keywords in the text.
        nlp_counts (int): Count of NLP-related keywords in the text.
        trad_ml_counts (int): Count of Traditional ML-related keywords in the text.
        others_counts (int): Count of keywords related to Other skills in the text.
        resume_keywords (dict): Dictionary of skill areas and their respective keywords.

    Returns:
        tuple: A tuple containing average scores for CV, NLP, Traditional ML, and Other skills.
    """
    field_keyword_counts = count_field_keywords(resume_keywords)
    cv_avg = (cv_counts / field_keyword_counts["CV"]) * 100
    nlp_avg = (nlp_counts / field_keyword_counts["NLP"]) * 100
    trad_ml_avg = (trad_ml_counts / field_keyword_counts["Tradition ML"]) * 100
    others_avg = (others_counts / field_keyword_counts["Other skills"]) * 100
    return cv_avg, nlp_avg, trad_ml_avg, others_avg


def calculate_scores(text, resume_dict):
    """
    Calculate the output scores for each skill area based on the input text.

    Calculates the scores for different skill areas (CV, NLP, Traditional ML, Other skills)
    based on the occurrence of keywords from the provided resume_dict dictionary in the input text.

    Args:
        text (str): Input text extracted from the PDF.
        resume_dict (dict): Dictionary of skill areas and their respective keywords.

    Returns:
        list: List of average scores for CV, NLP, Traditional ML, and Other skills.
    """
    # Initialize score counters for each area
    cv_counts = 0
    nlp_counts = 0
    trad_ml_counts = 0
    others_counts = 0

    # Obtain the scores for each area
    for area in resume_dict.keys():
        if area == "CV":
            for word in resume_dict[area]:
                if word in text:
                    cv_counts += 1
        elif area == "NLP":
            for word in resume_dict[area]:
                if word in text:
                    nlp_counts += 1
        elif area == "Tradition ML":
            for word in resume_dict[area]:
                if word in text:
                    trad_ml_counts += 1
        else:
            for word in resume_dict[area]:
                if word in text:
                    others_counts += 1
    cv_avg, nlp_avg, trad_ml_avg, others_avg = calculate_output_averages(
        cv_counts, nlp_counts, trad_ml_counts, others_counts, resume_dict
    )
    return [cv_avg, nlp_avg, trad_ml_avg, others_avg]


def save_plot(output_arr, out_dir="output"):
    """
    Generate and save a pie chart visualizing the scores.

    Generates a pie chart using Matplotlib to visualize the scores for different skill areas.
    The chart is saved as a .png file.

    Args:
        output_arr (list): List of average scores for CV, NLP, Traditional ML, and Other skills.
    """
    pie = plt.figure(figsize=(10, 10))
    plt.pie(
        np.array(output_arr) / 100,
        labels=["CV", "NLP", "Tradition ML", "Other skills"],
        explode=(0.1, 0, 0, 0),
        autopct="%1.0f%%",
        shadow=True,
        startangle=90,
    )
    plt.title("Machine Learning Engineering Candidate - Resume Decomposition by Areas")
    plt.axis("equal")
    # plt.show()
    # Save pie chart as a .png file
    pie.savefig(f"{out_dir}/pie_chart.png")


def save_csv(output, fields, out_dir="output"):
    """
    Save the output scores to a CSV file.

    Generates a CSV file containing the scores for different skill areas along with their labels.

    Args:
        output (list): List of average scores for CV, NLP, Traditional ML, and Other skills.
        fields (list): List of skill area labels.
    """
    summary = pd.DataFrame(output, index=fields, columns=["score"]).sort_values(
        by="score", ascending=False
    )
    summary.to_csv(f"{out_dir}/summary.csv")


def save_output(avg_res, terms):
    """
    Save the calculated output scores and visualizations.

    Saves the calculated average scores and generates a CSV summary and a pie chart visualization.

    Args:
        avg_res (list): List of average scores for CV, NLP, Traditional ML, and Other skills.
        terms (dict): Dictionary of skill areas and their respective keywords.
    """
    save_csv(avg_res, terms.keys())
    save_plot(avg_res)
    print("output saved in output directory...")
