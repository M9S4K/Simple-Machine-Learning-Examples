import tweepy #to access twitter API
from textblob import TextBlob

consumer_key = 'Ho09Wf2ZI88dGhQFx7h1ihtCz'
consumer_secret = 'P6cMA7maIX8SsCzLCMCJm5VokTf03fHDSPHF0MeflkJ1yYLhIP'

access_token = '24318160-CgTQDOLMFQ1MUfLUMPym6qAdYuOIwxW4EV9csFa2L'
access_token_secret = '4Azfm6cTocMQCUFepwgBnDEtJBP5uy8aQYYO0Xm2uG4KX'

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

