import json
import pandas as pd 
import pymongo
import re


conn=pymongo.MongoClient()
db = conn.test
collection = db.test_collection

tweets_data = []

cursor = collection.find()

results = [res for res in cursor]
cursor.close()
tweets = {"text": []}
dataset = pd.DataFrame()
for item in results:
	try:
		tweets["text"].append(item['text'])
	except:
		continue
# tweets = pd.DataFrame()
# tf = pd.DataFrame()
# for item in results:
# 		try:
# 			tweets["text"].append(item['text'])
# 		except:
# 			continue
# # tf = tweets
# print tweets
# print tf

tweets_hashtags = {'hashtags':[]}

for i in range(0,len(tweets["text"])):
	x = re.findall(r'[#]\S*', tweets["text"][i])
	tweets_hashtags['hashtags'].append(x)
# print tweets_hashtags
th = pd.DataFrame(tweets_hashtags['hashtags'])
# th.from_dict(tweets_hashtags)
# for i in range(0,len(tweets["text"])):
# 	try:
# 		th.concat(tweets_hashtags["hashtags"][i])
# 	except:
# 		continue
# th = tweets_hashtags.value_counts()
th = pd.value_counts(th.values.flatten())
th = th[:10]
print th