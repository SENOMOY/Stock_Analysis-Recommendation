import tweepy
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt


# Define twitter authentication variables
consumer_key = "D1grpQXVpRja1tfgEskvvJrbo"
consumer_secret = "skKgypeBSOAF8hsMml4wOelxmQEwyRIJ4zRl7cUUO4F3Pdko5I"
access_token = "1001831549753491457-xuxrBxvi2qLZbscpOZy3smzj66WZ2r"
access_token_secret = "fxvK7DZwlm1b5a0kKDxRaitO7W91xztKcHHpAMcnR3brX"
# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

def searchTweets(company):
    # Language code (follows ISO 639-1 standards)
    language = "en"
    # Calling the user_timeline function with our parameters
    tweets = api.search(q="\"" + company +"\"", rpp=10000,count=10000, result_type="recent", lang=language)
    toDataFrame(tweets).to_csv('data/tweets/'+company+'.csv')
    return tweets

def getSentimentResult(company):
    tweets = searchTweets(company)
    positive = 0
    negative = 0
    neutral = 0
    for tweet in tweets:
        text = tweet.text
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.0:
            positive += 1
        elif polarity < 0.0:
            negative += 1
        else:
            neutral += 1
    # Data to plot
    labels = 'Positive', 'Negative', 'Neutral'
    sizes = [positive, negative, neutral]
    colors = ['green', 'red', 'grey']
    explode = (0, 0, 0)  # explode 1st slice
    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    # Plot
    fig = plt.gcf()
    fig.canvas.set_window_title("Sentiment Analysis")
    plt.axis('equal')
    plt.show()
    plt.draw()
    return plt

def toDataFrame(tweets):

    DataSet = pd.DataFrame()

    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text for tweet in tweets]
    DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet in tweets]
    DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet in tweets]
    DataSet['tweetSource'] = [tweet.source for tweet in tweets]
    DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]
    DataSet['userID'] = [tweet.user.id for tweet in tweets]
    DataSet['userScreen'] = [tweet.user.screen_name for tweet in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    DataSet['userCreateDt'] = [tweet.user.created_at for tweet in tweets]
    DataSet['userDesc'] = [tweet.user.description for tweet in tweets]
    DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet in tweets]
    DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet in tweets]
    DataSet['userLocation'] = [tweet.user.location for tweet in tweets]
    DataSet['userTimezone'] = [tweet.user.time_zone for tweet in tweets]

    return DataSet