# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 13:28:10 2025

@author: esd96
"""
#setting up credientials
# -*- coding: utf-8 -*-

import requests
import json
import time 
import datetime 

# --- 1. CONFIGURATION AND CREDENTIALS ---

token = "AAAAAAAAAAAAAAAAAAAAAD9d5gEAAAAABMnj58kIBU1fk7S%2B5NAZGlZMxZg%3DpkoXZlITsOsEUarXiFzvnqbgdpespC1L7txz3NkyV30deBgw8F" 
URL = "https://api.twitter.com/2/tweets/search/recent"

HEADERS = {
    "Authorization": f"Bearer {token}"
}

# --- 2. QUERY 1: ARIZONA ---

search_az = 'climate change Arizona'
az_data = 'climate_change_Arizona_posts.jsonl'
params_az = { # Used a unique name for params
    'query': search_az,
    'max_results': 50,
    'tweet.fields': 'created_at,geo',
    'expansions': 'geo.place_id'
}

print(f"Searching for: {search_az}...")

try:
    response = requests.get(URL, headers=HEADERS, params=params_az)
    response.raise_for_status() # essential HTTP error check
    
    json_response = response.json()
    
    if 'data' in json_response:
        print(f"\n Found {len(json_response['data'])} matching posts.")
        
        with open(az_data, 'a', encoding='utf-8') as f:
            for tweet in json_response['data']:
                json.dump(tweet, f)
                f.write('\n')
                
    else:
        print("\n No posts matched the query criteria.")
        if 'errors' in json_response:
            print("\nAPI Errors:", json.dumps(json_response['errors'], indent=2))
            
            
    # --- RATE LIMIT CHECK (SUCCESSFUL RUN) ---
    remaining = response.headers.get('x-rate-limit-remaining')
    reset_timestamp = response.headers.get('x-rate-limit-reset')
    limit = response.headers.get('x-rate-limit-limit')

    if reset_timestamp:
        reset_time = datetime.datetime.fromtimestamp(int(reset_timestamp))
        
        print("-" * 30)
        print("API Rate Limit Status:")
        print(f"Limit for this window: {limit}")
        print(f"Requests Remaining: {remaining}")
        print(f"Limit Resets At: {reset_time.strftime('%Y-%m-%d %H:%M:%S MST')}")
        print("-" * 30)
            
except requests.exceptions.HTTPError as err:
    print(f"\n HTTP Error occurred: {err}")
    print("Check your Bearer Token or API access level.")
except Exception as err:
    print(f"\n An unexpected error occurred: {err}")


# --- PAUSE TO AVOID RATE LIMIT (CRITICAL FOR FREE TIER) ---
# FIX 3: Pause for 15 minutes (900 seconds) to reset the 1-request/15-min limit.
print("\n--- PAUSING: Waiting 901 seconds to reset Free Tier rate limit... ---")
time.sleep(900) 
print("--- RESUMING search. ---")


# --- 3. QUERY 2: IOWA ---

search_iowa = 'climate change Iowa'
iowa_data = 'climate_change_Iowa_posts.jsonl'
params_iowa = { # Used a unique name for params
    'query': search_iowa,
    'max_results': 50,
    'tweet.fields': 'created_at,geo',
    'expansions': 'geo.place_id'
}

print(f"Searching for: {search_iowa}...")

try:
    response = requests.get(URL, headers=HEADERS, params=params_iowa)
    response.raise_for_status() # essential HTTP error check
    
    json_response = response.json()
    
    if 'data' in json_response:
        print(f"\n Found {len(json_response['data'])} matching posts.")
        
        with open(iowa_data, 'a', encoding='utf-8') as f:
            for tweet in json_response['data']:
                json.dump(tweet, f)
                f.write('\n')
                
    else:
        print("\n No posts matched the query criteria.")
        if 'errors' in json_response:
            print("\nAPI Errors:", json.dumps(json_response['errors'], indent=2))
            
    # --- RATE LIMIT CHECK (SUCCESSFUL RUN) ---
    remaining = response.headers.get('x-rate-limit-remaining')
    reset_timestamp = response.headers.get('x-rate-limit-reset')
    limit = response.headers.get('x-rate-limit-limit')

    if reset_timestamp:
        reset_time = datetime.datetime.fromtimestamp(int(reset_timestamp))
        
        print("-" * 30)
        print("API Rate Limit Status:")
        print(f"Limit for this window: {limit}")
        print(f"Requests Remaining: {remaining}")
        print(f"Limit Resets At: {reset_time.strftime('%Y-%m-%d %H:%M:%S MST')}")
        print("-" * 30)
            
except requests.exceptions.HTTPError as err:
    print(f"\n HTTP Error occurred: {err}")
    print("Check your Bearer Token or API access level.")
except Exception as err:
    print(f"\n An unexpected error occurred: {err}")

print("\nProcessing complete.")

# --- 3. QUERY 3: FLORIDA ---

search_florida = 'climate change Florida'
florida_data = 'climate_change_Florida_posts.jsonl'
params_florida = { # Used a unique name for params
    'query': search_florida,
    'max_results': 50,
    'tweet.fields': 'created_at,geo',
    'expansions': 'geo.place_id'
}

print(f"Searching for: {search_florida}...")

try:
    response = requests.get(URL, headers=HEADERS, params=params_florida)
    response.raise_for_status() # essential HTTP error check
    
    json_response = response.json()
    
    if 'data' in json_response:
        print(f"\n Found {len(json_response['data'])} matching posts.")
        
        with open(florida_data, 'a', encoding='utf-8') as f:
            for tweet in json_response['data']:
                json.dump(tweet, f)
                f.write('\n')
                
    else:
        print("\n No posts matched the query criteria.")
        if 'errors' in json_response:
            print("\nAPI Errors:", json.dumps(json_response['errors'], indent=2))
            
    # --- RATE LIMIT CHECK (SUCCESSFUL RUN) ---
    remaining = response.headers.get('x-rate-limit-remaining')
    reset_timestamp = response.headers.get('x-rate-limit-reset')
    limit = response.headers.get('x-rate-limit-limit')

    if reset_timestamp:
        reset_time = datetime.datetime.fromtimestamp(int(reset_timestamp))
        
        print("-" * 30)
        print("API Rate Limit Status:")
        print(f"Limit for this window: {limit}")
        print(f"Requests Remaining: {remaining}")
        print(f"Limit Resets At: {reset_time.strftime('%Y-%m-%d %H:%M:%S MST')}")
        print("-" * 30)
            
except requests.exceptions.HTTPError as err:
    print(f"\n HTTP Error occurred: {err}")
    print("Check your Bearer Token or API access level.")
except Exception as err:
    print(f"\n An unexpected error occurred: {err}")

print("\nProcessing complete.")


# --- 2. CONFIGURATION AND CREDENTIALS ---

token = "AAAAAAAAAAAAAAAAAAAAAM4D5wEAAAAABAY40FR7KJvxzVy8nECM2RMKj9A%3DpikJQpMKp37qIm3IPhAbbPKbwARnN2pREdR5mewvrmtCcMRo7J" 
URL = "https://api.twitter.com/2/tweets/search/recent"

HEADERS = {
    "Authorization": f"Bearer {token}"
}

# --- 2. QUERY 4: Washington ---

search_w = 'climate change Washington'
w_data = 'climate_change_Washington_posts.jsonl'
params_w = { # Used a unique name for params
    'query': search_w,
    'max_results': 50,
    'tweet.fields': 'created_at,geo',
    'expansions': 'geo.place_id'
}

print(f"Searching for: {search_w}...")

try:
    response = requests.get(URL, headers=HEADERS, params=params_w)
    response.raise_for_status() # essential HTTP error check
    
    json_response = response.json()
    
    if 'data' in json_response:
        print(f"\n Found {len(json_response['data'])} matching posts.")
        
        with open(w_data, 'a', encoding='utf-8') as f:
            for tweet in json_response['data']:
                json.dump(tweet, f)
                f.write('\n')
                
    else:
        print("\n No posts matched the query criteria.")
        if 'errors' in json_response:
            print("\nAPI Errors:", json.dumps(json_response['errors'], indent=2))
            
            
    # --- RATE LIMIT CHECK (SUCCESSFUL RUN) ---
    remaining = response.headers.get('x-rate-limit-remaining')
    reset_timestamp = response.headers.get('x-rate-limit-reset')
    limit = response.headers.get('x-rate-limit-limit')

    if reset_timestamp:
        reset_time = datetime.datetime.fromtimestamp(int(reset_timestamp))
        
        print("-" * 30)
        print("API Rate Limit Status:")
        print(f"Limit for this window: {limit}")
        print(f"Requests Remaining: {remaining}")
        print(f"Limit Resets At: {reset_time.strftime('%Y-%m-%d %H:%M:%S MST')}")
        print("-" * 30)
            
except requests.exceptions.HTTPError as err:
    print(f"\n HTTP Error occurred: {err}")
    print("Check your Bearer Token or API access level.")
except Exception as err:
    print(f"\n An unexpected error occurred: {err}")


# --- PAUSE TO AVOID RATE LIMIT (CRITICAL FOR FREE TIER) ---
# FIX 3: Pause for 15 minutes (900 seconds) to reset the 1-request/15-min limit.
print("\n--- PAUSING: Waiting 901 seconds to reset Free Tier rate limit... ---")
time.sleep(900) 
print("--- RESUMING search. ---")


# --- 3. QUERY 5: New York ---

search_ny = 'climate change New York'
ny_data = 'climate_change_New_York_posts.jsonl'
params_ny = { # Used a unique name for params
    'query': search_ny,
    'max_results': 50,
    'tweet.fields': 'created_at,geo',
    'expansions': 'geo.place_id'
}

print(f"Searching for: {search_ny}...")

try:
    response = requests.get(URL, headers=HEADERS, params=params_ny)
    response.raise_for_status() # essential HTTP error check
    
    json_response = response.json()
    
    if 'data' in json_response:
        print(f"\n Found {len(json_response['data'])} matching posts.")
        
        with open(ny_data, 'a', encoding='utf-8') as f:
            for tweet in json_response['data']:
                json.dump(tweet, f)
                f.write('\n')
                
    else:
        print("\n No posts matched the query criteria.")
        if 'errors' in json_response:
            print("\nAPI Errors:", json.dumps(json_response['errors'], indent=2))
            
    # --- RATE LIMIT CHECK (SUCCESSFUL RUN) ---
    remaining = response.headers.get('x-rate-limit-remaining')
    reset_timestamp = response.headers.get('x-rate-limit-reset')
    limit = response.headers.get('x-rate-limit-limit')

    if reset_timestamp:
        reset_time = datetime.datetime.fromtimestamp(int(reset_timestamp))
        
        print("-" * 30)
        print("API Rate Limit Status:")
        print(f"Limit for this window: {limit}")
        print(f"Requests Remaining: {remaining}")
        print(f"Limit Resets At: {reset_time.strftime('%Y-%m-%d %H:%M:%S MST')}")
        print("-" * 30)
            
except requests.exceptions.HTTPError as err:
    print(f"\n HTTP Error occurred: {err}")
    print("Check your Bearer Token or API access level.")
except Exception as err:
    print(f"\n An unexpected error occurred: {err}")

print("\nProcessing complete.")