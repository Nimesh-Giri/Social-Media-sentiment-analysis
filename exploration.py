import pandas as pd

file_path = 'archive/Tweets.csv'

try:
    df = pd.read_csv(file_path)
    print("CSV loaded successfully!\n")
except Exception as e:
    print("Error loading CSV:", e)
    exit()

print("First 5 rows:")
print(df.head(), "\n")

print("Data info:")
print(df.info(), "\n")

print("Missing values per column:")
print(df.isnull().sum(), "\n")

# Check if column exists before printing value counts
if 'airline_sentiment' in df.columns:
    print("Sentiment distribution:")
    print(df['airline_sentiment'].value_counts())
else:
    print("Column 'airline_sentiment' not found in CSV!")
