import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = 'c:/Data_Analytics/cleaned_data.csv'
df = pd.read_csv(file_path)

# Set the style of the plots
sns.set(style="whitegrid")

# Plot Total Spend vs. Age
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Total Spend', hue='Satisfaction Level', data=df)
plt.title('Total Spend vs. Age')
plt.savefig('c:/Data_Analytics/total_spend_vs_age.png')
plt.show()

# Plot Average Rating by Gender
plt.figure(figsize=(8, 5))
sns.boxplot(x='Gender', y='Average Rating', data=df)
plt.title('Average Rating by Gender')
plt.savefig('c:/Data_Analytics/avg_rating_by_gender.png')
plt.show()
