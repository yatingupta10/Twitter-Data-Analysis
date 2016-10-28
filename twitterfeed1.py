import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
from pymongo import MongoClient
import json


#consumer key, consumer secret, access token, access secret.
ckey="sdCz9kjLtiQ98HBAVunKgXoaA"
consumer_secret="TicRxrGbE38SVx376WXqLP9E9riVJmqGZPiaWuFvqjZ2cM9ZEu"
access_token_key="764873117613391872-hHtgIyAsKqGOKNDM8XBzyGHfJz5Yagg"
access_token_secret="pNzPwmwhOGuPDOQsWPnWFjn7UvDpGETQ5Vy383CbNDS8x"

#client = MongoClient()

#client = MongoClient('localhost', 27017)

#db = client.test_database

#collection = db.test_collection 
start_time = time.time() #grabs the system time
keyword_list = ['#USelection']

class listener(StreamListener):
 
	def __init__(self, start_time, time_limit=60):
	 
		self.time = start_time
		self.limit = time_limit
		 
	def on_data(self, data):
	 
		while (time.time() - self.time) < self.limit:
		 
			try:
			 
			 
				client = MongoClient('localhost', 27017)
				db = client['twitter_db']
				collection = db['twitter_collection']
				tweet = json.loads(data)
				 
				collection.insert(tweet)
				#collection.find()
				tweets_iterator = collection.find()
				for tweet in tweets_iterator:
					print tweet['text']
				return True
				 
			 
			except BaseException, e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass
				 
				exit()
		 
	def on_error(self, status):
		print statuses


auth = OAuthHandler(ckey, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)


twitterStream = Stream(auth, listener(start_time, time_limit=20)) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream Object
