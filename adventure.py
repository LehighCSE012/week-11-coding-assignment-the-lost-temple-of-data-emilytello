"""
Practice reading structured data from Excel (.xlsx) files using Pandas.
Practice reading structured data from Tab-Separated Value (.tsv) files using Pandas.
Practice handling specific Pandas reading options (sheet_name, skiprows, sep).
Practice using Regular Expressions (re module) to find and extract specific patterns (dates, codes)
from text data.
Practice writing functions with clear inputs and outputs suitable for automated testing.
"""
import pandas as pd
import re
def load_artifact_data(excel_filepath):
    """
    Reads artifact data from a specific sheet ('Main Chamber') in an Excel file,
    skipping the first 3 rows.
    """
    df = pd.read_excel(excel_filepath, sheet_name='Main Chamber', skiprows=3)
    return df
def load_location_notes(tsv_filepath):
    """
    Reads location data from a Tab-Separated Value (TSV) file.
    """
    df = pd.read_csv(tsv_filepath, sep='\t')
    return df
def extract_journal_dates(journal_text):
    """
    Extracts all dates in MM/DD/YYYY format from the journal text.
    """
    pattern = r'\b((0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4})\b'
    matches = re.findall(pattern, journal_text)
    return [m[0] for m in matches]
def extract_secret_codes(journal_text):
    """
    Extracts all secret codes in AZMAR-XXX format (XXX are digits)
    from the journal text.
    """
    pattern = r'\bAZMAR-\d{3}\b'
    return re.findall(pattern, journal_text)
if __name__ == '__main__':
    EXCEL_FILE = 'artifacts.xlsx'
    TSV_FILE = 'locations.tsv'
    JOURNAL_FILE = 'journal.txt'
    print(f"--- Loading Artifact Data from {EXCEL_FILE} ---")
    try:
        artifacts_df = load_artifact_data(EXCEL_FILE)
        print("Successfully loaded DataFrame. First 5 rows:")
        print(artifacts_df.head())
        print("\nDataFrame Info:")
        artifacts_df.info()
    except FileNotFoundError:
        print(f"Error: File not found at {EXCEL_FILE}")
    print(f"\n--- Loading Location Notes from {TSV_FILE} ---")
    try:
        locations_df = load_location_notes(TSV_FILE)
        print("Successfully loaded DataFrame. First 5 rows:")
        print(locations_df.head())
        print("\nDataFrame Info:")
        locations_df.info()
    except FileNotFoundError:
        print(f"Error: File not found at {TSV_FILE}")
    print(f"\n--- Processing Journal from {JOURNAL_FILE} ---")
    try:
        with open(journal_file, 'r', encoding='utf-8') as f:
            journal_content = f.read()
        print("\nExtracting Dates...")
        dates = extract_journal_dates(journal_content)
        print(f"Found dates: {dates}")
        print("\nExtracting Secret Codes...")
        codes = extract_secret_codes(journal_content)
        print(f"Found codes: {codes}")
    except FileNotFoundError:
        print(f"Error: File not found at {JOURNAL_FILE}")
        
