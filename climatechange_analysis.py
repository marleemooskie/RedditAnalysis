'''
In this file, we will load in the data and perform sentiment analysis.

'''
import os
import pandas as pd
import load_data
import sentimentAnalysis
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

# Load in the data
az_path = "/Users/marleeyork/Documents/RedditAnalysis/climate_change_Arizona_posts.pkl"
ia_path = "/Users/marleeyork/Documents/RedditAnalysis/climate_change_Iowa_posts.pkl"

AZ_df = load_data(az_path,location="AZ")
IA_df = load_data(ia_path,location="IA")

# Concat the dataframes
df = pd.concat([AZ_df,IA_df])

# Create sentiment class
sentiment1 = sentiment(df)

# Analyze sentiment of each tweet
sentiment1.analyze_sentiment()

# Plot these scores over time
plt.subplots()
plt.scatter(sentiment1.date,sentiment1.compound_score)
plt.show()

# Find the top sentiments of each tweet, grouping by location
sentiment1.find_top_sentiments()

# Find the number of positive, negative, and neutral sentiments
# Group this by location as well
sentiment1.count_sentiments(location_group=True) 
sentiment1.sentiment_counts

# Unpack the counts into a dataframe and plot as a barplot
df_counts = pd.DataFrame(
    [(loc, sent, count) for (loc, sent), count in sentiment1.sentiment_counts.items()],
    columns=['Location', 'Sentiment', 'Count']
)

# Pivot the data so rows = location, columns = sentiment
plot_df = df_counts.pivot(index='Location', columns='Sentiment', values='Count').fillna(0)

# Stacked bar plot
plot_df.plot(
    kind='bar',
    stacked=True,
    figsize=(8,5)
)

plt.xlabel("Location")
plt.ylabel("Count")
plt.title("Sentiment Counts by Location")
plt.legend(title="Sentiment")
plt.tight_layout()
plt.show()

