# import pandas as pd

# # Load the CSV data
# def load_data(file_path):
#     try:
#         # Use the absolute path here
#         data = pd.read_csv(file_path, encoding='ISO-8859-1')  # Modify encoding as necessary
#         return data
#     except Exception as e:
#         print(f"Error loading data: {e}")
#         return None  # Return None if loading fails

# # Clean and preprocess the data
# def clean_data(data):
#     data.drop_duplicates(inplace=True)
#     data.dropna(inplace=True, how='any')
#     print("Unique values in 'Launch Date' before cleaning:")
#     print(data['Launch Date'].unique())
#     data['Launch Date'] = pd.to_datetime(data['Launch Date'], errors='coerce')
#     data.dropna(subset=['Launch Date'], inplace=True)
#     return data

# # Analyze the data
# def analyze_data(data):
#     total_launches = data.shape[0]
#     print(f"Total launches: {total_launches}")

#     if total_launches > 0:  # Only perform analysis if there are launches
#         successful_launches = data[data['Remarks'] == 'Launch successful'].shape[0]
#         print(f"Successful launches: {successful_launches}")
#         unsuccessful_launches = total_launches - successful_launches
#         print(f"Unsuccessful launches: {unsuccessful_launches}")
        
#         most_common_launch_vehicle = data['Launch Vehicle'].value_counts().idxmax()
#         print(f"Most common launch vehicle: {most_common_launch_vehicle}")
        
#         most_common_application = data['Application'].value_counts().idxmax()
#         print(f"Most common application: {most_common_application}")
        
#         most_common_orbit_type = data['Orbit Type'].value_counts().idxmax()
#         print(f"Most common orbit type: {most_common_orbit_type}")

# def main():
#     # Use an absolute path to the CSV file
#     file_path = r'E:\Codes\Global Space Exploration Progress Tracker\dataset\ISRO mission launches.csv'
#     data = load_data(file_path)
    
#     if data is not None:
#         print(f"Initial number of rows: {data.shape[0]}")
#         data = clean_data(data)
#         print(f"Number of rows after cleaning: {data.shape[0]}")
#         analyze_data(data)

# if __name__ == "__main__":
#     main()



import pandas as pd
import logging
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path: str) -> Optional[pd.DataFrame]:
    """Load CSV data from the given file path."""
    try:
        data = pd.read_csv(file_path, encoding='ISO-8859-1')  # Modify encoding as necessary
        logging.info("Data loaded successfully.")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """Clean and preprocess the data."""
    initial_shape = data.shape
    data.drop_duplicates(inplace=True)
    data.dropna(inplace=True, how='any')
    logging.info(f"Data shape before cleaning: {initial_shape}, after cleaning: {data.shape}")

    if 'Launch Date' in data.columns:
        logging.info("Unique values in 'Launch Date' before cleaning:")
        logging.info(data['Launch Date'].unique())
        data['Launch Date'] = pd.to_datetime(data['Launch Date'], errors='coerce')
        data.dropna(subset=['Launch Date'], inplace=True)

    return data

def analyze_data(data: pd.DataFrame):
    """Analyze the cleaned data."""
    total_launches = data.shape[0]
    logging.info(f"Total launches: {total_launches}")

    if total_launches > 0:  # Only perform analysis if there are launches
        successful_launches = data[data['Remarks'] == 'Launch successful'].shape[0]
        logging.info(f"Successful launches: {successful_launches}")
        unsuccessful_launches = total_launches - successful_launches
        logging.info(f"Unsuccessful launches: {unsuccessful_launches}")
        
        most_common_launch_vehicle = data['Launch Vehicle'].value_counts().idxmax()
        logging.info(f"Most common launch vehicle: {most_common_launch_vehicle}")
        
        most_common_application = data['Application'].value_counts().idxmax()
        logging.info(f"Most common application: {most_common_application}")
        
        most_common_orbit_type = data['Orbit Type'].value_counts().idxmax()
        logging.info(f"Most common orbit type: {most_common_orbit_type}")

        # Optionally, provide some summary statistics
        logging.info("Summary statistics of the data:")
        logging.info(data.describe(include='all'))

def main(file_path: str):
    """Main function to load, clean, and analyze data."""
    data = load_data(file_path)
    
    if data is not None:
        logging.info(f"Initial number of rows: {data.shape[0]}")
        data = clean_data(data)
        logging.info(f"Number of rows after cleaning: {data.shape[0]}")
        analyze_data(data)

if __name__ == "__main__":
    # Use an absolute path to the CSV file
    file_path = r'launches.csv'
    main(file_path)
