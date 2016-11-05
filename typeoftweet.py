import json
import pandas as pd
import pymongo


def types_of_tweet():
    conn = pymongo.MongoClient()
    db = conn.test
    collection = db.test_collection

    cursor = collection.find()

    results = [res for res in cursor]
    cursor.close()
    text_count = 0
    image_count = 0
    text_and_image_count = 0
    for item in results:
        try:
            if item['text']:
                text_count = text_count + 1
                if item['entities']['media']:
                    text_and_image_count = text_and_image_count + 1
            elif item['entities']['media']:
                image_count = image_count + 1
        except:
            continue

    list_of_counts = [text_count, image_count, text_and_image_count]

    return list_of_counts
