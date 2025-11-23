# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 13:28:10 2025

@author: esd96
"""

import requests
import json

#setting up credientials
token = "AAAAAAAAAAAAAAAAAAAAAD9d5gEAAAAABMnj58kIBU1fk7S%2B5NAZGlZMxZg%3DpkoXZlITsOsEUarXiFzvnqbgdpespC1L7txz3NkyV30deBgw8F" 

# Base URL for the Recent Search endpoint (up to 7 days of posts)
URL = "https://api.twitter.com/2/tweets/search/recent"

# Combined topic and location query
# Searching for "wildfire" posts within flagstaff and phoenix's bounding box
# --- Query 1: Flagstaff ---
search_flag = 'wildfire bounding_box:-112.11 34.94 -111.17 35.47'
flag_data = 'wildfire_flagstaff_posts.jsonl'
# Parameters for the API call
params = {
    'query': search_flag,
    'max_results': 50,  # Number of posts to retrieve
    'tweet.fields': 'created_at,geo', # Request the timestamp and geo details
    'expansions': 'geo.place_id' # Request place details to be included in the 'includes' section
}

headers = {
    "Authorization": f"Bearer {token}"
}

# --- 2. API request for Flagstaff ---
print(f"Searching for: {search_flag}...")

try:
    response = requests.get(URL, headers=headers, params=params)
    
    json_response = response.json()

    # --- PROCESS THE RESULTS ---
    
    if 'data' in json_response:
        print(f"\n Found {len(json_response['data'])} matching posts.")
        
        with open(flag_data, 'a', encoding='utf-8') as f:
            for tweet in json_response['data']:
                # Write each post as a separate JSON line
                json.dump(tweet, f)
                f.write('\n')
                
    else:
        print("\n No posts matched the query criteria.")
        # Print error details if present
        if 'errors' in json_response:
             print("\nAPI Errors:")
             print(json.dumps(json_response['errors'], indent=2))
        
except requests.exceptions.HTTPError as err:
    print(f"\n HTTP Error occurred: {err}")
    print("Bearer Token and API access level failed.")
except Exception as err:
    print(f"\n An error occurred: {err}")


# --- Query 2: Phoenix ---
search_phx = 'wildfire bounding_box:-112.84 32.97 -111.17 33.85'
phx_data = 'wildfire_phoenix_posts.jsonl'
# Parameters for the API call
params = {
    'query': search_phx,
    'max_results': 1,  # Number of posts to retrieve
    'tweet.fields': 'created_at,geo', # Request the timestamp and geo details
    'expansions': 'geo.place_id' # Request place details to be included in the 'includes' section
}

headers = {
    "Authorization": f"Bearer {token}"
}

# --- 2. API request for Phoenix ---
print(f"Searching for: {search_phx}...")

try:
    response = requests.get(URL, headers=headers, params=params)
    
    json_response = response.json()

    # --- PROCESS THE RESULTS ---
    
    if 'data' in json_response:
        print(f"\n Found {len(json_response['data'])} matching posts.")
        
        with open(phx_data, 'a', encoding='utf-8') as f:
            for tweet in json_response['data']:
                # Write each post as a separate JSON line
                json.dump(tweet, f)
                f.write('\n')
                
    else:
        print("\n No posts matched the query criteria.")
        # Print error details if present
        if 'errors' in json_response:
             print("\nAPI Errors:")
             print(json.dumps(json_response['errors'], indent=2))
        
except requests.exceptions.HTTPError as err:
    print(f"\n HTTP Error occurred: {err}")
    print("Bearer Token and API access level failed.")
except Exception as err:
    print(f"\n An error occurred: {err}")


#code to see how many requests remaining
remaining = response.headers.get('x-rate-limit-remaining')
reset_timestamp = response.headers.get('x-rate-limit-reset')
limit = response.headers.get('x-rate-limit-limit')

import datetime
# Convert the Unix timestamp to a readable time
if reset_timestamp:
    reset_time = datetime.datetime.fromtimestamp(int(reset_timestamp))
    
    print("-" * 30)
    print("API Rate Limit Status:")
    print(f"Limit for this window: {limit}")
    print(f"Requests Remaining: {remaining}")
    print(f"Limit Resets At: {reset_time.strftime('%Y-%m-%d %H:%M:%S MST')}")
    print("-" * 30)