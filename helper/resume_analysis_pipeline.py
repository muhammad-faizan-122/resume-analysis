from .utils import (
    load_yml_cfgs,
    extract_text,
    preprocess,
    calculate_scores,
    save_output,
)


def perform_resume_analysis():
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
    # Step 1: load configs
    keywords = load_yml_cfgs("config/keywords.yml")

    # Step 2: Extract text from PDF
    text = extract_text(keywords["resume_path"])

    # Step 3: Process text
    processed_text = preprocess(text)

    # Step 4: Calculate output
    avg_res_list = calculate_scores(processed_text, keywords["technical_fields"])

    # Step 5: Save output
    save_output(avg_res_list, keywords["technical_fields"])
