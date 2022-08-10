#if the followers follows are more than 100

import tweepy 

auth = tweepy.OAuthHandler('K4V9p9uCH4pPJFmYByS9Oznvr','EN2EZMyqkuSaNrbQXhEHuFuBTqf7h98arjuDEEKSKnmUTchmvC')
auth.set_access_token('2796301290-EqHi4lYNWzbXki0Z9YxlX5OxADaU4zyFZz20zBo','3atx0d5vwevTelJvg07Jl42nAPJS0gh88CflAfVDSxYWL')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(1000)

for follower in tweepy.Cursor(api.followers).items():
	if follower.followers_count > 100:
		follower.follow()
		print("Sucess")
		break