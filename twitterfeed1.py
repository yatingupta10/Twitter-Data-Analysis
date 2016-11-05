import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
from pymongo import MongoClient
import json


# consumer key, consumer secret, access token, access secret.
ckey = "sdCz9kjLtiQ98HBAVunKgXoaA"
consumer_secret = "TicRxrGbE38SVx376WXqLP9E9riVJmqGZPiaWuFvqjZ2cM9ZEu"
access_token_key = "764873117613391872-hHtgIyAsKqGOKNDM8XBzyGHfJz5Yagg"
access_token_secret = "pNzPwmwhOGuPDOQsWPnWFjn7UvDpGETQ5Vy383CbNDS8x"


class listener(StreamListener):

    def on_data(self, data):

            # while (time.time() - self.time) < self.limit:

        try:
            saveFile = open('twitdb.csv', 'a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True

        except BaseException as e:
            print 'failed ondata,', str(e)
            time.sleep(5)

    def on_error(self, status):
        print status


auth = OAuthHandler(ckey, consumer_secret)  # OAuth object
auth.set_access_token(access_token_key, access_token_secret)


twitterStream = Stream(auth, listener())
twitterStream.filter(track=['#USelection'])
