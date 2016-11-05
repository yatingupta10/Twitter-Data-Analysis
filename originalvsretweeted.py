import json
import pandas as pd
import pymongo


def original_vs_retweet():
    conn = pymongo.MongoClient()
    db = conn.test
    collection = db.test_collection

    cursor = collection.find()

    results = [res for res in cursor]
    cursor.close()
    tweets = {"entities": []}
    for item in results:
        try:
                # checking whether tweet is retweeted or not
            if item['retweeted_status']:
                tweets["entities"].append(True)
        except:
            tweets["entities"].append(False)
    original_vs_retweeted_df = pd.DataFrame(tweets['entities'])
    original_vs_retweeted_df = pd.value_counts(
        original_vs_retweeted_df.values.flatten())
    original_vs_retweeted_count = original_vs_retweeted_df.reset_index().values.tolist()
    true_count = original_vs_retweeted_count[0][1]
    false_count = original_vs_retweeted_count[1][1]
    list_of_counted_values = [true_count, false_count]

    return list_of_counted_values
