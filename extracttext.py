import json
import pandas as pd 
import matplotlib.pyplot as plt
from io import StringIO

def text_count():
	hc = 0
	dt = 0
	#hilarylist = ["#HilaryClinton", "Hilary", "Clinton"]
	#donaldlist = ["#DonaldTrump", "Donlald", "Trump"]
	for i in range(0,len(tt)):
		# text_count = tt[i]
		# print tt[i]
		if "#Clinton" in tt[i]:
			hc = hc + 1
		elif "#Trump" in tt[i]:
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
#tweets["country"] = map(lambda tweet:tweet['place']['country']if['place']!=None else None,tweets_data)
#tweets_by_country = tweets['country'].value_counts()
tt = tweets["text"]
# tweets_by_lang = tweets['lang'].value_counts()
# print tweets_by_lang

tweets_by_text = text_count()

#print tweets_by_text
fig,ax = plt.subplots()
ax.tick_params(axis = 'x', labelsize = 15)
ax.tick_params(axis = 'y', labelsize = 10)
ax.set_xlabel('countries', fontsize = 15)
ax.set_xlabel('number of tweets', fontsize = 15)
ax.set_title('Top 5 countries', fontsize = 15, fontweight = 'bold')
tweets_by_text["Hilary", "Trump"].plot(ax = ax, kind = 'bar', color = 'red')
#print tweets["text"]
plt.show()
