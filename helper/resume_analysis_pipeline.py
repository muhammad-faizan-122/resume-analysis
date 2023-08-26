from .utils import *
import yaml


with open("config/keywords.yml", "r") as keywords_json:
    keywords = yaml.safe_load(keywords_json)["technical_fields"]


def run():
    """
    Main function to execute the PDF text processing workflow.

    This function follows these steps:
    1. Reads the input PDF.
    2. Extracts text from the PDF.
    3. Processes the extracted text.
    4. Calculates and retrieves the output.
    5. Saves the output.

    Requires:
    - Input reading functions from `input_reading` module.
    - Text processing functions from `text_processing` module.
    - Output manipulation functions from `output_manupulation` module.
    - A `config/keywords.yml` file with keywords for output calculation.

    """
    # Step 1: Read input PDF
    pdf_reader = read_input_pdf()

    # Step 2: Extract text from PDF
    text = text_extraction(pdf_reader)

    # Step 3: Process text
    processed_text = text_processing(text)

    # Step 4: Calculate output
    avg_res_list = output_calculation(processed_text, keywords)

    # Step 5: Save output
    save_output(avg_res_list, keywords)
