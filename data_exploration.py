import pandas as pd

# Load the dataset into a DataFrame
file_path = 'C:/Data_Analytics/E-commerce Customer Behavior.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())

# Display the column names
print("Column Names:")
print(df.columns)

# Get a summary of the dataset
print("\nDataset Summary:")
print(df.info())

# Generate descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe(include='all'))

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
