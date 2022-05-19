
#%%
import pandas as pd
import numpy as np
import tweepy
import twitter_credentials

#%%
#Authorizations of Keys and Tokens for Twitter API Project
auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET, twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth) 

client = tweepy.Client(bearer_token=twitter_credentials.BEARER_TOKEN)

# %%
query = "luka OR luka doncic"

response = client.search_recent_tweets(query=query, max_results=10)


for tweet in response.data:
    print(tweet.text)
# %%
