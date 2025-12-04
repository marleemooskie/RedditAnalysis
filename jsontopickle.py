# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 14:41:49 2025

@author: esd96
"""

#json to pickle

import pandas as pd
import json
import os

def jsonl_to_pickle(input_file_path, output_file_path):
    """
    Converts a JSON Lines (.jsonl) file into a Python list of dictionaries
    and saves it as a Pickle (.pkl) file.
    
    Args:
        input_file_path (str): The path to the source .jsonl file.
        output_file_path (str): The path where the .pkl file will be saved.
    """
    if not os.path.exists(input_file_path):
        print(f"Error: Input file not found at {input_file_path}")
        return

    data_list = []
    
    # 1. Read the .jsonl file line by line
    print(f"Loading data from {input_file_path}...")
    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Each line is a single JSON object (a single post)
                data_list.append(json.loads(line))
        
        # 2. Convert the list of dictionaries into a pandas DataFrame
        df = pd.DataFrame(data_list)
        
        # 3. Save the DataFrame to a Pickle file
        df.to_pickle(output_file_path)
        
        print(f"Conversion complete. Data saved to {output_file_path}")
        print(f"Total records saved: {len(df)}")
        
    except Exception as e:
        print(f"An error occurred during processing: {e}")


# Define the file names
AZ_JSONL_FILE = 'climate_change_Arizona_posts.jsonl'
AZ_PICKLE_FILE = 'climate_change_Arizona_posts.pkl'

IOWA_JSONL_FILE = 'climate_change_Iowa_posts.jsonl'
IOWA_PICKLE_FILE = 'climate_change_Iowa_posts.pkl'

FLORIDA_JSONL_FILE = 'climate_change_Florida_posts.jsonl'
FLORIDA_PICKLE_FILE = 'climate_change_Florida_posts.pkl'

WASH_JSONL_FILE = 'climate_change_Washington_posts.jsonl'
WASH_PICKLE_FILE = 'climate_change_Washington_posts.pkl'

NY_JSONL_FILE = 'climate_change_New_York_posts.jsonl'
NY_PICKLE_FILE = 'climate_change_New_York_posts.pkl'

# Run the conversion for the Arizona data
jsonl_to_pickle(AZ_JSONL_FILE, AZ_PICKLE_FILE)

# Run the conversion for the Iowa data
jsonl_to_pickle(IOWA_JSONL_FILE, IOWA_PICKLE_FILE)

# Run the conversion for the Florida data
jsonl_to_pickle(FLORIDA_JSONL_FILE, FLORIDA_PICKLE_FILE)

# Run the conversion for the Washington data
jsonl_to_pickle(WASH_JSONL_FILE, WASH_PICKLE_FILE)

# Run the conversion for the New York data
jsonl_to_pickle(NY_JSONL_FILE, NY_PICKLE_FILE)