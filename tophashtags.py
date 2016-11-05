import json
import pandas as pd
import pymongo
import re


def top_ten_hashtags():
    conn = pymongo.MongoClient()
    db = conn.test
    collection = db.test_collection

    tweets_data = []

    cursor = collection.find()

    results = [res for res in cursor]
    cursor.close()
    tweets = {"text": []}
    for item in results:
        try:
            tweets["text"].append(item['text'])
        except:
            continue
    tweets_hashtags = {'hashtags': []}

    for i in range(0, len(tweets["text"])):
        x = re.findall(r'[#]\S*', tweets["text"][i])
        tweets_hashtags['hashtags'].append(x)
    hashtags_df = pd.DataFrame(tweets_hashtags['hashtags'])
    hashtags_df = pd.value_counts(hashtags_df.values.flatten())
    hashtags_df = hashtags_df.reset_index().values.tolist()
    hashtags_df = hashtags_df[:11]
    return hashtags_df
