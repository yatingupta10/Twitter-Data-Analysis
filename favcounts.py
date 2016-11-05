import json
import pandas as pd
import pymongo


def favorite_counts():
    conn = pymongo.MongoClient()
    db = conn.test
    collection = db.test_collection

    cursor = collection.find()

    results = [res for res in cursor]
    cursor.close()
    fav_count = [['Tweet ID', 'Favorite Count']]
    for item in results:
        count = 0
        try:
                # checking whether tweet is retweeted or not
            if item['retweeted_status']:
                count = item['retweeted_status']['favorite_count']
            if item['quoted_status']:
                count += item['quoted_status']['favorite_count']
            fav_count.append([str(item['id']), count])
        except:
            continue
    return fav_count
