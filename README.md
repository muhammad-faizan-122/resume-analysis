# Resume Analysis  

A simple yet effective resume analysis tool that extracts text from PDF resumes and performs keyword-based analysis. This project follows a traditional approach to identify relevant information based on predefined keywords. You to add keyword in inside the `config/keywords.yaml' which want to check in resume.


## How to Use  

1. **Set up the environment:**  
   Run the following command to create a virtual environment  
   ```
   python3 -m venv venv
   ```  

2. **Prepare the resume for analysis:**  
   - Place the PDF resume in the **`input`** directory.  
   - Update the resume path name in **`config/keywords.yml`**.  

3. **Run the analysis:**  
   Execute the script using:  
   ```bash
   python3 main.py
   ```  

4. **Output**
   Output will save in the Pie-chart and .CSV format in `output` directory
   
   ![Pie-chart Representation](output/pie_chart.png)
This tool provides a foundation for automated resume analysis, allowing for easy customization to fit various domains. 🚀