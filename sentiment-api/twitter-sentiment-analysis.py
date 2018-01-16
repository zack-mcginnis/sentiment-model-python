import tweepy
from textblob import TextBlob
import config

consumer_key = config.API_CONFIG['consumer_key']
consumer_secret = config.API_CONFIG['consumer_secret']

access_token = config.API_CONFIG['access_token']
access_token_secret = config.API_CONFIG['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Ethereum')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment);
