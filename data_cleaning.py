import pandas as pd

# Load the dataset
file_path = 'C:/Data_Analytics/E-commerce Customer Behavior.csv'
df = pd.read_csv(file_path)

# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Option 1: Drop rows with missing values (for simplicity)
df_cleaned = df.dropna()

# Option 2: Fill missing values
# Fill numeric columns with the mean
numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Fill non-numeric columns with the mode (most frequent value)
non_numeric_cols = df.select_dtypes(exclude=['number']).columns
for col in non_numeric_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Check for duplicates
print("Duplicate rows in the dataset:")
print(df.duplicated().sum())

# Remove duplicate rows
df_cleaned = df.drop_duplicates()

# Save the cleaned data to a new CSV file
df_cleaned.to_csv('c:/Data_Analytics/cleaned_data.csv', index=False)

# Print the cleaned dataset
print("Cleaned data sample:")
print(df_cleaned.head())
