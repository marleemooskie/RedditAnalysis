# This file is loading in and organizing the twitter pickle into a dataframe
import pandas as pd
import pickle

def load_data(data_pickle,location):
    """
    Parameters
    ----------
    data_pickle : TYPE
        DESCRIPTION. Pathway for pickle file of twitter data.
    location : TYPE
        DESCRIPTION. What location this data was scraped for specifically.

    Returns
    -------
    data : TYPE
        DESCRIPTION. Dataframe of tweets cleaned for sentiment analysis by VADER.
        VADER supports hashtags, punctuations, and even emojis, so these were left in.

    """
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
    
    # Add a location column
    data['Location'] = [location] * data.shape[0]
    
    return data
        