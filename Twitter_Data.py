import tweepy

# Define twitter authentication variables
consumer_key = "RY5Fa3leByq7gNEdxEs1LJ00O"
consumer_secret = "hgpVP5bf7GKHs6ayRfYDC75roArAVEYv9gG8LmwyfNlKyYw4kQ"
access_token = "432489536-E2EiHmiz8mK0vCAXxWUxB9w2IovU5Xrc04vs9Fh1"
access_token_secret = "z7hcfoaVgMRpZEiHnpRPGGKBiYWjXql1vQ6tDvIRIfJa1"
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
        print(type[results])
        for tweet in results:
            # printing the text stored inside the tweet object
            print(tweet.text)


searchTweets(["microsoft"])