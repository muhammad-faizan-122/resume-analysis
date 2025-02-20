# Resume Analysis  

A simple yet effective resume analysis tool that extracts text from PDF resumes and performs keyword-based analysis. This project follows a traditional approach to identify relevant information based on predefined keywords.

**Note:** This implementation is tailored for resumes in the AI field. To adapt it for other domains, update the keywords in **`config/keywords.yml`** accordingly.  

## How to Use  

1. **Set up the environment:**  
   Run the following command to create a Conda environment from the provided `environment.yml` file:  
   ```bash
   conda env create -f environment.yml
   ```  

2. **Prepare the resume for analysis:**  
   - Place the PDF resume in the **`input`** directory.  
   - Update the resume file name in **`config/resume_path.yml`**.  

3. **Run the analysis:**  
   Execute the script using:  
   ```bash
   python3 main.py
   ```  

This tool provides a foundation for automated resume analysis, allowing for easy customization to fit various domains. 🚀