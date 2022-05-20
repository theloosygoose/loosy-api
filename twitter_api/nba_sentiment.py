
#%%
import pandas as pd
import numpy as np
import tweepy
import twitter_credentials
import re

#%%
#Authorizations of Keys and Tokens for Twitter API Project
auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET, twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth) 

client = tweepy.Client(bearer_token=twitter_credentials.BEARER_TOKEN)

# %%
query = "luka lang:en OR luka doncic lang:en"

response = client.search_recent_tweets(query=query, max_results=10)

i = 1
for tweet in response.data:
    print(str(i) + ". " + tweet.text + "\n" )
    i = i + 1
# %%
#Create a DataFrame with column called Tweets

df = pd.DataFrame( [tweet.text for tweet in response.data], columns=['Tweets'])
# %%
#Cleaning Data
#Cleaning function
def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9_:]+', '', text) #Removes @mentions
    text = re.sub(r'#', '', text) #removes hashtag symbols
    text = re.sub(r'RT[\s]+', '', text) #removes RT
    text = re.sub(r'https?:\/\/\S+', '', text)
    text = re.sub(r'\n', ' ', text)
    return text

#Cleaning the Text
df['Tweets'] = df['Tweets'].apply(cleanTxt)

#Show the cleaned text
# %%
