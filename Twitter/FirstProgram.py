import tweepy 

auth = tweepy.OAuthHandler('K4V9p9uCH4pPJFmYByS9Oznvr','EN2EZMyqkuSaNrbQXhEHuFuBTqf7h98arjuDEEKSKnmUTchmvC')
auth.set_access_token('2796301290-EqHi4lYNWzbXki0Z9YxlX5OxADaU4zyFZz20zBo','3atx0d5vwevTelJvg07Jl42nAPJS0gh88CflAfVDSxYWL')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)