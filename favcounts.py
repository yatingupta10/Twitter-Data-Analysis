import json
import pandas as pd 
import pymongo


def favorite_counts():
	conn=pymongo.MongoClient()
	db = conn.test
	collection = db.test_collection

	cursor = collection.find()

	results = [res for res in cursor]
	cursor.close()
	fav_count = [['Tweet ID', 'Favorite Count']]
	for item in results:
		count = 0
		try:
			if item['retweeted_status']:	#checking whether tweet is retweeted or not
				count = item['retweeted_status']['favorite_count']
			if item['quoted_status']:
				count += item['quoted_status']['favorite_count']
			fav_count.append([str(item['id']), count])
		except:
			continue
	return fav_count
# print len(fav_count["favorite_counts"])
# original_vs_retweeted_df = pd.DataFrame(fav_count['entities'])
# original_vs_retweeted_df = pd.value_counts(original_vs_retweeted_df.values.flatten())
# original_vs_retweeted_count = original_vs_retweeted_df.reset_index().values.tolist()
# true_count = original_vs_retweeted_count[0][1]
# false_count = original_vs_retweeted_count[1][1]
# list_of_counted_values = [true_count, false_count]
