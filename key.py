import twitter

auth = twitter.OAuth(consumer_key="",
consumer_secret="",
token="",
token_secret="")

tw = twitter.Twitter(auth=auth)