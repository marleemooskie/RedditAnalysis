'''
This script includes the function to perform sentiment analysis using VADER on
a string of text.
'''
import nltk
import pandas as pd
nltk.download("vader_lexicon")
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
sia = SentimentIntensityAnalyzer()

class sentiment:
    def __init__(self, df):
        self.id = df.id
        self.edit_history_tweet_ids = df.edit_history_tweet_ids
        self.date = df.date
        self.Location = df.Location
        self.text = df.text
        self.sentiment_scores = []
        self.top_sentiments = []
        self.sentiment_counts = {}
        self.positive_score = []
        self.negative_score = []
        self.compound_score = []
    
    def analyze_sentiment(self):
        '''
        Returns
        -------
        TYPE List of dictionaries including positive, neutral, negative, and compound scores.
            DESCRIPTION. This returns the VADER sentiment analysis scores for each
            text string inputted and stores it under self.sentiment_scores.
        '''
        # Loop through each string in text list and perform sentiment analysis
        self.sentiment_scores = [sia.polarity_scores(t) for t in self.text]
        # Extract the positive, negative, and compound scores for each
        positive_score = []
        negative_score = []
        compound_score = []
        for score in self.sentiment_scores:
            positive_score.append(score['pos'])
            negative_score.append(score['neg'])
            compound_score.append(score['compound'])
        self.positive_score = positive_score
        self.negative_score = negative_score
        self.compound_score = compound_score
        
        print("Retrieving sentiment: ")
        # Store this into the class
        return self.sentiment_scores
    
    def find_top_sentiments(self):
        '''
        Returns
        -------
        top_sentiments : TYPE List of top sentiment scores for each text string.
            DESCRIPTION. Usees the compound score to find the overall sentiment
            of the text string.
        '''
        top_sentiments = []
        # Loop through each text string
        for sentiment_dict in self.sentiment_scores:
            compound_score = sentiment_dict['compound']
            # If compound score is less than -.05 its negative
            if (compound_score <= -.05):
                top_sentiment = 'Negative'
            # If compound score is greater than .05 its positive
            elif (compound_score >= .05):
                top_sentiment = 'Positive'
            # Otherwise, its neutral
            else:
                top_sentiment = 'Neutral'
            # Add top sentiment to the list of all top sentiments
            top_sentiments.append(top_sentiment)
        self.top_sentiments = top_sentiments
        return top_sentiments
    
    def count_sentiments(self, location_group=False):
        '''
        Parameters
        ----------
        group_by : TYPE String of a variable name
            DESCRIPTION. A variable we want to group counts by.
            
        Returns
        -------
        counts : TYPE Dictionary of counts for each sentiment type.
            DESCRIPTION. Counts how many negative, positive, and neutral tweets
            there are in the list of text strings.
        '''
        if location_group:
            data = pd.DataFrame({'Location':self.Location,'top_sentiments':self.top_sentiments})
            counts = Counter((row.Location, row.top_sentiments) for row in data.itertuples())
        else:
            counts = Counter(self.top_sentiments)
        self.sentiment_counts = counts

        return counts
        
