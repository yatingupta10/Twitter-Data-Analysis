import json
import pandas as pd
import pymongo


def location_of_tweet():
    conn = pymongo.MongoClient()
    db = conn.test
    collection = db.test_collection

    cursor = collection.find()

    results = [res for res in cursor]
    cursor.close()
    tweets = {"places": []}
    for item in results:
        try:
            tweets["places"].append(item['place']['country_code'])
        except:
            continue
    country_count = [["Country", "Count"]]
    location_df = pd.DataFrame(tweets['places'])
    location_df = pd.value_counts(location_df.values.flatten())
    country_count += location_df.reset_index().values.tolist()
    return country_count
