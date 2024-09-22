import pandas as pd
import re

def clean_user_data(input_file, output_file='new_data.csv', chunksize=10000):
    # Define a more comprehensive regex pattern for validating email addresses
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Initialize an empty DataFrame to collect cleaned data
    cleaned_data = pd.DataFrame()

    # Step 1: Read the CSV file in chunks
    for chunk in pd.read_csv(input_file, chunksize=chunksize):
        # Remove duplicates based on 'user_id'
        chunk = chunk.drop_duplicates(subset='user_id', keep='first')
        
        # Filter rows with valid email addresses
        chunk = chunk[chunk['email'].apply(lambda x: bool(re.match(email_pattern, x)))]

        # Append cleaned chunk to the main DataFrame
        cleaned_data = pd.concat([cleaned_data, chunk], ignore_index=True)

    # Step 5: Write the cleaned data to a new CSV file (default is new_data.csv)
    cleaned_data.to_csv(output_file, index=False)
    print(f"Cleaned data has been saved to {output_file}")

# Example usage
input_file = 'user_data.csv'  # Input CSV file with user data
clean_user_data(input_file)
