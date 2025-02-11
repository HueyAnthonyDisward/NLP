import pandas as pd
from datasets import load_dataset

# Load the SMS Spam Collection dataset
sms_spam = load_dataset('codesignal/sms-spam-collection')

# Convert to pandas DataFrame properly
df = sms_spam['train'].to_pandas()

# Count the number of unique messages and labels
print("Unique messages:", df['message'].nunique(), "\n")

# Returns the unique labels
print("Labels:", df['label'].unique(), "\n")
