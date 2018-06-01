import tweepy #to access twitter API
from textblob import TextBlob

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'

access_token = 'your_access_token'
access_token_secret = 'your_token_secret'

#Authentication, logging in via code
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#Search a bunch of tweets that has the word
#Trump and store that list of tweets
public_tweets = api.search('Trump')

for tweet in public_tweets:         #for each tweet in public_tweets
    print(tweet.text)               #each tweet has a text attribute   
    analysis = TextBlob(tweet.text) #analysis of tweet.text
    print(analysis.sentiment)       #print sentiment attr of analysis var

