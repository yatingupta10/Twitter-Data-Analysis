import json
import pandas as pd 
import matplotlib.pyplot as plt
from io import StringIO

def text_count():
	hc = 0
	dt = 0
	hillarylist = ["#HillaryClinton", "Hillary", "Clinton", "#Hillary", "#Clinton", "HillaryClinton", "hillaryclinton", "hillary clinton", "Hillary Clinton"]
	donaldlist = ["#DonaldTrump", "#Donlald", "#Trump", "Donald", "Trump", "DonaldTrump", "donaldtrump", "donald trump", "Donald Trump"]
	for i in range(0,len(tt)):
		# text_count = tt[i]
		# print tt[i]
		if "#HillaryClinton" in tt[i] or "Hillary" in tt[i] or "Clinton" in tt[i] or "#Hillary" in tt[i] or "#Clinton" in tt[i] or "HillaryClinton" in tt[i] or "hillaryclinton" in tt[i] or "hillary clinton" in tt[i] or  "Hillary Clinton" in tt[i]:
			hc = hc + 1
		elif "#DonaldTrump" in tt[i] or "Donald" in tt[i] or "Trump" in tt[i] or "#Donald" in tt[i] or "#Trump" in tt[i] or "DonaldTrump" in tt[i] or "donaldtrump" in tt[i] or "donald trump" in tt[i] or  "Donald Trump" in tt[i]:
			dt = dt + 1
	
	listcount = [hc, dt]
	#print listcount
	return listcount



tweets_data_path = "twitdb.txt"
tweets_data = []


tweets_file = open(tweets_data_path, 'r')

for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except:
		continue

tweets = pd.DataFrame()
tt = pd.DataFrame()
tweets["text"] = map(lambda tweet:tweet['text'],tweets_data)
tweets["lang"] = map(lambda tweet:tweet['lang'],tweets_data)
tt = tweets["text"]

tweets_by_text = text_count()

labels = 'Hillary Clinton', 'Donald Trump'

plt.pie(tweets_by_text, labels=labels, startangle=90)
plt.axis('equal')
plt.show()
