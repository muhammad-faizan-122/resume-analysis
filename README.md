# resume-analysis
Basic anaysis on input resume using traditional way, to extract the pdf text from it and give output on performing operation on base of keywords. 
Note: I worked on resume analysis of AI feild, you have modify code and keyword in **config/keywords.yml** according to your use case. 
## Usage
- run the conda environment.yaml, it will create the conda env using following command
    ```
    conda env create -f environment.yml
    ```
- place pdf resume in **input** directory
- update the name of resume in **config/resume_path.yml**
- run code using following command 
    ```
    python3 main.py
    ```