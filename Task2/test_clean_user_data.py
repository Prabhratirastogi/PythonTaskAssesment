import unittest
import pandas as pd
import os
from task_1_clean_user_data import clean_user_data  # Import your function

class TestCleanUserData(unittest.TestCase):

    def setUp(self):
        # Create a temporary CSV file for testing
        self.input_file = 'test_user_data.csv'
        self.output_file = 'test_cleaned_data.csv'
        
        # Create a sample input CSV with valid and invalid email addresses
        data = {
            'user_id': [1, 2, 3, 4, 1],  # Duplicate user_id
            'email': [
                'valid.email@example.com',
                'invalid.email@.com',
                'another.valid@example.com',
                'invalid.email@domain',
                'valid.email@example.com'  # Duplicate email
            ]
        }
        df = pd.DataFrame(data)
        df.to_csv(self.input_file, index=False)

    def tearDown(self):
        # Clean up: remove the temporary files
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_clean_user_data(self):
        # Call the function to clean user data
        clean_user_data(self.input_file, self.output_file)

        # Read the cleaned data
        cleaned_data = pd.read_csv(self.output_file)

        # Check if the cleaned data has the expected number of rows
        self.assertEqual(len(cleaned_data), 2)  # Expecting 2 valid entries

        # Check if the cleaned data contains the correct valid emails
        expected_emails = [
            'valid.email@example.com',
            'another.valid@example.com'
        ]
        self.assertTrue(all(email in cleaned_data['email'].values for email in expected_emails))

if __name__ == '__main__':
    unittest.main()
