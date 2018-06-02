import tweepy
import pandas as pd

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

def searchTweets(company_list):
    for company in company_list:
        # Language code (follows ISO 639-1 standards)
        language = "en"
        # Calling the user_timeline function with our parameters
        result = api.search(q="\"" + company +"\"", rpp=1000,count=1000, result_type="recent", lang=language)
        toDataFrame(result).to_csv('tweets/'+company+'.csv')

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