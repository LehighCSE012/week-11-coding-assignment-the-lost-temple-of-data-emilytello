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
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    return re.findall(pattern, journal_text)
def extract_secret_codes(journal_text):
    """
    Extracts all secret codes in AZMAR-XXX format (XXX are digits)
    from the journal text.
    """
    pattern = r'\bAZMAR-\d{3}\b'
    return re.findall(pattern, journal_text)
if __name__ == '__main__':
    excel_file = 'artifacts.xlsx'
    tsv_file = 'locations.tsv'
    journal_file = 'journal.txt'
    print(f"--- Loading Artifact Data from {excel_file} ---")
    try:
        artifacts_df = load_artifact_data(excel_file)
        print("Successfully loaded DataFrame. First 5 rows:")
        print(artifacts_df.head())
        print("\nDataFrame Info:")
        artifacts_df.info()
    except FileNotFoundError:
        print(f"Error: File not found at {excel_file}")
    print(f"\n--- Loading Location Notes from {tsv_file} ---")
    try:
        locations_df = load_location_notes(tsv_file)
        print("Successfully loaded DataFrame. First 5 rows:")
        print(locations_df.head())
        print("\nDataFrame Info:")
        locations_df.info()
    except FileNotFoundError:
        print(f"Error: File not found at {tsv_file}")
    print(f"\n--- Processing Journal from {journal_file} ---")
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
        print(f"Error: File not found at {journal_file}")
        