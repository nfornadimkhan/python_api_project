import requests
import pandas as pd
from datetime import datetime
from typing import Dict, Any


# Task 1: Here my approch is to write a function and return a dictionary with the document information.

def get_presidential_document(start_date: str, end_date: str, nth_document: int) -> Dict[Any, Any]:
    """
    Problem: To get a specific presidential document information in a specific time period?
    
    Args:
        start_date (str): Start date in format 'DD.MM.YYYY'
        end_date (str): End date in format 'DD.MM.YYYY'
        nth_document (int): Position of document to retrieve (1-based index)
        
    Returns:
        dict: Document information including title, abstract, publication date, document number, and type
    """

    URL = "https://www.federalregister.gov/api/v1/documents"
    
    # As I see the API requires dates in YYYY-MM-DD format, convert dates to API format (YYYY-MM-DD)
    # I find solution here: 😀
    # https://stackoverflow.com/questions/502726/converting-date-between-dd-mm-yyyy-and-yyyy-mm-dd

    start = datetime.strptime(start_date, '%d.%m.%Y').strftime('%Y-%m-%d')
    end = datetime.strptime(end_date, '%d.%m.%Y').strftime('%Y-%m-%d')
    
    params = {
        'conditions[type][]': 'PRESDOCU',
        'conditions[publication_date][gte]': start,
        'conditions[publication_date][lte]': end,
        'per_page': 20,  # Changed from 1 to 20 to get more results per request
        'page': 1,       # Always get first page
        'order': 'oldest'
    }
    
    response = requests.get(f"{URL}", params=params)
    
    # Debug information
    print(f"\nFetching documents...")
    print(f"URL being called: {response.url}")
    print(f"Total documents available: {response.json().get('count', 'Not available')}")
    
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
        
    data = response.json()
    
    if len(data['results']) > 0:
        # Get the nth document from results if available
        if nth_document <= len(data['results']):
            doc = data['results'][nth_document - 1]  # Adjust for 0-based index
            return {
                'number': nth_document,
                'title': doc['title'],
                'abstract': doc['abstract'],
                'publication_date': doc['publication_date'],
                'document_number': doc['document_number'],
                'type': doc['type']
            }
    return None  # No document found at this position

# Task 2: Extract document data for the first 20 documents from 1st December 2010 to 31st December 2010
def main():
    documents = []
    try:
        # Get first 20 documents
        for i in range(1, 20):  # 1 to 20
            doc = get_presidential_document('01.12.2010', '31.12.2010', i)
            if doc is not None:  # Only append if document was found
                documents.append(doc)
        
        if not documents:  # Check if we found any documents
            print("No documents found in the specified time period")
            return
            
        # Create DataFrame from the list of documents
        df = pd.DataFrame(documents)
        
        # Print the DataFrame
        print("\nPresidential Documents (1st Dec 2010 to 31st Dec 2010):")
        print(df)
        
        # Save to data to CSV
        df.to_csv('presidential_documents.csv', index=False)
        print("\nData saved to presidential_documents.csv")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()