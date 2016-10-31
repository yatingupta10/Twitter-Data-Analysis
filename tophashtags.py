import json
import pandas as pd 
import matplotlib.pyplot as plt
import re

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
tf = pd.DataFrame()
tweets["text"] = map(lambda tweet:tweet['text'],tweets_data)
tf = tweets["text"]

tweets_hashtags = {'hashtags':[]}

for i in range(0, len(tf)):
	x = re.findall(r'[#]\S*', tf[i])
	tweets_hashtags['hashtags'].append(x)
th = pd.DataFrame()
#th = tweets_hashtags['hashtags']
th = tweets_hashtags['hashtags'].value_counts()
print th

# fig,ax = plt.subplots()
# ax.tick_params(axis = 'x', labelsize = 200)
# ax.tick_params(axis = 'y', labelsize = 10)
# ax.set_xlabel('places', fontsize = 15)
# ax.set_xlabel('number of tweets', fontsize = 15)
# ax.set_title('Location of the tweets', fontsize = 15, fontweight = 'bold')
# tweets_by_hashtags[:10].plot(ax = ax, kind = 'bar', color = 'red')
# plt.show()