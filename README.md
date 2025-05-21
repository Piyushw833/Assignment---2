# XYZ TECH Vehicle Insurance Claims Analysis

This project analyzes vehicle insurance claims data from XYZ TECH, an Indian insurance provider. The analysis focuses on claims filed during April 2025, examining patterns in claim amounts, premiums, payment status, and rejection reasons.

## Project Overview

The project consists of three main components:
1. **Data Preprocessing**: Pure Python implementation for cleaning and validating data
2. **City Analysis**: Analysis of operations in Pune, Kolkata, Ranchi, and Guwahati
3. **Rejection Classification**: Classification of claim rejection reasons

## Dataset Information
The dataset (`Insurance_auto_data.csv`) includes:
- Claim ID and dates
- Customer information
- Claim amounts
- Premium details
- Payment status
- Rejection reasons (if applicable)
- City information

## Project Structure
```
Project 2/
├── notebooks/
│   └── insurance_analysis.ipynb    # Main analysis notebook
├── src/
│   ├── city_analyzer.py           # City analysis implementation
│   ├── pure_data_processor.py     # Data preprocessing module
│   └── rejection_classifier.py     # Rejection classification module
├── insurance_claims_analysis output pdf        # Output Notebook File in PDF Format
├── Insurance_auto_data.csv        # Input data file
├── README.md                      # This file
└── requirements.txt               # Python dependencies
```

## Setup Instructions

1. **Python Environment Setup**:
   Make sure you have Python 3.8 or higher installed. You can check your Python version with:
   ```bash
   python --version
   ```

2. **Create Virtual Environment** (recommended):
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install LaTeX** (required for PDF generation):
   - Windows: Install MiKTeX from https://miktex.org/download
   - Linux: `sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic`
   - Mac: Install MacTeX from https://www.tug.org/mactex/

## Running the Analysis

1. **Prepare Data**:
   - Ensure `Insurance_auto_data.csv` is in the project root directory
   - The file should contain the required columns (CLAIM_ID, CLAIM_DATE, etc.)

2. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

3. **Run the Analysis**:
   - Navigate to `notebooks/insurance_analysis.ipynb`
   - Click "Kernel" → "Restart & Run All" to execute all cells

4. **Generate PDF Report**:
   ```bash
   # Method 1: Using command line
   jupyter nbconvert --to pdf notebooks/insurance_analysis.ipynb

   # Method 2: From Jupyter interface
   # File → Download as → PDF via LaTeX
   ```

   The PDF will be generated as `notebooks/insurance_analysis.pdf`

## Output and Results

The analysis notebook and PDF will include:
1. **Data Quality Report**:
   - Missing value statistics
   - Invalid record counts
   - Data type validations

2. **City Analysis**:
   - Performance metrics for each city
   - Recommendation for city closure
   - Supporting data and visualizations

3. **Rejection Analysis**:
   - Classification of rejection reasons
   - Distribution of rejection categories
   - City-wise rejection patterns

## PDF Generation Troubleshooting

If you encounter issues generating the PDF:

1. **LaTeX Installation**:
   - Verify LaTeX is installed: `latex --version`
   - For Windows: Restart after MiKTeX installation
   - For Linux: Install additional packages if needed:
     ```bash
     sudo apt-get install texlive-latex-extra
     ```

2. **Common PDF Issues**:
   - If images don't render: Run notebook cells before conversion
   - If fonts are missing: Install recommended fonts package
   - If conversion fails: Check Jupyter logs for specific errors

3. **Alternative PDF Methods**:
   - Print to PDF from browser (less formatted but works without LaTeX)
   - Export to HTML then convert to PDF using browser
   - Use online Jupyter notebook viewers with PDF export

## Additional Notes

- The analysis uses pure Python implementation without pandas/numpy dependencies
- All data processing is done in memory
- For large datasets, ensure sufficient system memory is available
- The PDF report includes all code, outputs, and visualizations

## Contact

For any questions or issues, please contact the XYZ TECH data science team. 
