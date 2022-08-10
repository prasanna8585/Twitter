#like the post based on keywords

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

search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search,search_string).items(numbersOfTweets):
	try:
		tweet.favorite()
		print('I Liked that tweet !')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break