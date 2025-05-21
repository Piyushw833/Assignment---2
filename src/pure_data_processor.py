from typing import List, Dict, Union, Any, Optional
from datetime import datetime
import csv
import re

class InsuranceDataPreprocessor:
    """Pure Python class for preprocessing insurance claims data without external libraries."""
    
    def __init__(self, file_path: str):
        """Initialize the preprocessor with file path."""
        self.file_path = file_path
        self.headers = []
        self.data = []
        
    def read_csv(self) -> None:
        """Read CSV file and store headers and data."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                self.headers = next(csv_reader)  # Get headers
                self.data = [row for row in csv_reader]
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")
        except Exception as e:
            raise Exception(f"Error reading CSV file: {str(e)}")

    def clean_numeric(self, value: str) -> Union[float, str]:
        """Clean numeric values by removing currency symbols and converting to float."""
        if not value or value.strip() == '':
            return 0.0
        
        # Remove currency symbols and commas using regex
        cleaned = re.sub(r'[₹$,]', '', value).strip()
        try:
            return float(cleaned)
        except ValueError:
            return value

    def validate_date(self, date_str: str) -> str:
        """Validate and standardize date format."""
        if not date_str or date_str.strip() == '':
            return ''
        
        try:
            # Try different date formats
            for fmt in ['%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y', '%Y/%m/%d']:
                try:
                    date_obj = datetime.strptime(date_str, fmt)
                    return date_obj.strftime('%Y-%m-%d')
                except ValueError:
                    continue
            return date_str
        except Exception:
            return date_str

    def clean_text(self, text: str) -> str:
        """Clean text fields by removing special characters and standardizing."""
        if not text or text.strip() == '':
            return ''
        
        # Remove extra whitespace and special characters
        cleaned = ' '.join(text.split())
        return cleaned

    def process_data(self) -> Dict[str, List[Any]]:
        """Process and clean the data."""
        self.read_csv()
        
        # Initialize dictionary to store cleaned data
        cleaned_data = {header: [] for header in self.headers}
        
        # Process each row
        for row in self.data:
            for i, value in enumerate(row):
                header = self.headers[i]
                
                # Apply appropriate cleaning based on column type
                if header in ['CLAIM_AMOUNT', 'PREMIUM_COLLECTED', 'PAID_AMOUNT']:
                    cleaned_value = self.clean_numeric(value)
                elif header in ['CLAIM_DATE']:
                    cleaned_value = self.validate_date(value)
                elif header in ['REJECTION_REMARKS', 'CITY']:
                    cleaned_value = self.clean_text(value)
                else:
                    cleaned_value = value if value else ''
                
                cleaned_data[header].append(cleaned_value)
        
        return cleaned_data

    def get_cleaned_data(self) -> List[Dict[str, Any]]:
        """Return cleaned data as a list of dictionaries."""
        cleaned_dict = self.process_data()
        
        # Convert to list of dictionaries format
        num_rows = len(next(iter(cleaned_dict.values())))
        cleaned_list = []
        
        for i in range(num_rows):
            row_dict = {}
            for header in self.headers:
                row_dict[header] = cleaned_dict[header][i]
            cleaned_list.append(row_dict)
        
        return cleaned_list

    def validate_row(self, row: Dict[str, Any]) -> bool:
        """Validate a single row of data."""
        # Check for required fields
        required_fields = ['CLAIM_AMOUNT', 'PREMIUM_COLLECTED', 'CITY']
        for field in required_fields:
            if field not in row or not row[field]:
                return False
        
        # Validate claim amount and premium
        if not isinstance(row['CLAIM_AMOUNT'], (int, float)) or row['CLAIM_AMOUNT'] < 0:
            return False
        if not isinstance(row['PREMIUM_COLLECTED'], (int, float)) or row['PREMIUM_COLLECTED'] < 0:
            return False
        
        return True

    def get_statistics(self) -> Dict[str, Any]:
        """Calculate basic statistics from the cleaned data."""
        cleaned_data = self.get_cleaned_data()
        
        stats = {
            'total_records': len(cleaned_data),
            'cities': set(),
            'total_claim_amount': 0,
            'total_premium': 0,
            'missing_values': {},
            'invalid_records': 0
        }
        
        for row in cleaned_data:
            if self.validate_row(row):
                stats['cities'].add(row['CITY'])
                stats['total_claim_amount'] += float(row['CLAIM_AMOUNT'])
                stats['total_premium'] += float(row['PREMIUM_COLLECTED'])
            else:
                stats['invalid_records'] += 1
            
            # Count missing values
            for key, value in row.items():
                if not value:
                    stats['missing_values'][key] = stats['missing_values'].get(key, 0) + 1
        
        stats['cities'] = list(stats['cities'])
        return stats 