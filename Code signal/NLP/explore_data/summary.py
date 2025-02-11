import pandas as pd
from datasets import load_dataset

# Load the SMS Spam Collection dataset
sms_spam = load_dataset('codesignal/sms-spam-collection')

# Convert to pandas DataFrame for convenient handling
df = pd.DataFrame(sms_spam['train'])

# Display the DataFrame's detailed information
df.info()

# Print all columns present in the DataFrame
print("Columns in the dataset:", df.columns.tolist())

# Count and print the number of unique messages in the dataset
print("Number of unique messages:", df['sms'].nunique())

# Identify and print the unique labels found in the dataset
print("Unique labels:", df['label'].unique())

# Display basic descriptive statistics of the DataFrame
print(df.describe(include='all'))
