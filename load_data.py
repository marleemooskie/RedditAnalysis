# This file is loading in and organizing the twitter pickle into a dataframe
import pandas as pd
import pickle

def load_data(data_pickle):
    # Load the pickle in
    with open("climate_change_Arizona_posts.pkl", "rb") as f:
        data = pickle.load(f)
    
    # Change the date into a date format
    dates = []
    for date in data.created_at:
        date_fixed = date[0:10]
        date_fixed = pd.to_datetime(date_fixed,format='%Y-%m-%d')
        dates.append(date_fixed)
    data['date'] = dates
    
    # Remove any taglines out of the text
    data["text"] = data["text"].str.replace(r"@\S+", "", regex=True)
    
    # Remove any \n from the text
    data["text"] = data["text"].str.replace("\n", "", regex=True)
        