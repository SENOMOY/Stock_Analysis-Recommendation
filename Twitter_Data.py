import tweepy

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
        results = api.search(q=company, rpp=1000,count=1000, result_type="recent", lang=language)
        for tweet in results:
            # printing the text stored inside the tweet object
            print(tweet.text)

searchTweets(["microsoft"])