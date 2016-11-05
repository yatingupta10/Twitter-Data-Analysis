import json
import pandas as pd
import pymongo


def text_count(tweets):
    hillary_score = 0
    donald_score = 0
    for i in range(0, len(tweets["text"])):
        if "#HillaryClinton" in tweets["text"][i] or "Hillary" in tweets["text"][i] or "Clinton" in tweets["text"][i] or "#Hillary" in tweets["text"][i] or "#Clinton" in tweets["text"][
                i] or "HillaryClinton" in tweets["text"][i] or "hillaryclinton" in tweets["text"][i] or "hillary clinton" in tweets["text"][i] or "Hillary Clinton" in tweets["text"][i]:
            hillary_score = hillary_score + 1
        elif "#DonaldoTrump" in tweets["text"][i] or "Donald" in tweets["text"][i] or "Trump" in tweets["text"][i] or "#Donald" in tweets["text"][i] or "#Trump" in tweets["text"][i] or "DonaldTrump" in tweets["text"][i] or "donaldtrump" in tweets["text"][i] or "donald trump" in tweets["text"][i] or "Donald Trump" in tweets["text"][i]:
            donald_score = donald_score + 1

    list_count = [hillary_score, donald_score]
    return list_count


def pop():
    conn = pymongo.MongoClient()
    db = conn.test
    collection = db.test_collection

    cursor = collection.find()

    results = [res for res in cursor]
    cursor.close()
    tweets = {"text": []}
    for item in results:
        try:
            tweets["text"].append(item['text'])
        except:
            continue
    popular_count = text_count(tweets)
    return popular_count
