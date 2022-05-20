
#%%
import pandas as pd
import numpy as np
import tweepy
from textblob import TextBlob
import config
import re

#%%
#Authorizations of Keys and Tokens for Twitter API Project
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth) 

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

# %%
query = "luka lang:en OR luka doncic lang:en"
response = client.search_recent_tweets(query=query, max_results=10, expansions='author_id')

#%%
users = {u["id"]: u for u in response.includes['users']}
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
#create a function to get the subjectivity
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
    return TextBlob(text).sentiment.polarity

df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
df['Polarity'] = df['Tweets'].apply(getPolarity)

df
# %%
