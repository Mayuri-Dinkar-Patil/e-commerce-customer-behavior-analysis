import pandas as pd

# Specify the full path to your dataset using forward slashes, double backslashes, or raw string notation
file_path = 'C:/Data_Analytics/E-commerce Customer Behavior.csv'
# Alternatively:
# file_path = 'C:\\Data_Analytics\\E-commerce_Customer_Behavior.csv'
# file_path = r'C:\Data_Analytics\E-commerce_Customer_Behavior.csv'

# Load the dataset into a DataFrame
try:
    df = pd.read_csv(file_path)
    # Display the first few rows of the dataset
    print(df.head())
except FileNotFoundError:
    print("The file was not found. Please check the path and file name.")
except Exception as e:
    print(f"An error occurred: {e}")

