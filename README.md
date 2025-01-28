# Federal Register API Data Extraction Project

## Project Overview
This project involves working with the Federal Register API to extract and analyze presidential document information. The Federal Register API is provided by the Office of the Federal Register (OFR) of the National Archives and Records Administration (NARA) and the U.S. Government Publishing Office (GPO) to make government decision-making more accessible to citizens.

## Objectives
1. Create a function to extract presidential document information using the Federal Register API
2. Extract and store data for multiple presidential documents within a specified time period
3. Learn to work with REST APIs and handle JSON responses
4. Practice data manipulation and storage in Python

## Features
### 1. Document Information Extraction Function
- Takes start date, end date, and document number as input
- Retrieves presidential document details via API
- Returns document number, title, and three additional characteristics

### 2. Batch Data Processing
- Extracts data for first 20 presidential documents
- Time period: 01.12.2010-31.12.2010
- Stores information in a structured format

### 3. Data Storage
- Creates a DataFrame with document information
- Exports data to Excel/CSV format
- Includes columns for document number, title, and other characteristics

## Technical Requirements
- Python programming language
- Required libraries:
  - requests (for API calls)
  - pandas (for data manipulation)
  - json (for handling API responses)

## API Information
- API Documentation: https://www.federalregister.gov/developers/documentation/api/v1/
- Endpoint parameters include:
  - Date range
  - Document type (PRESDOCU)
  - Other filtering options

## Learning Outcomes
1. Understanding of RESTful API integration
2. Experience with data extraction and transformation
3. Knowledge of working with JSON data
4. Practice with pandas DataFrame operations
5. File I/O operations in Python

## Institution Information
University of Hohenheim  