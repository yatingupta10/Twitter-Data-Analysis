import json
import pandas as pd 
import matplotlib.pyplot as plt

tweets_data_path = "twitdb.txt"
tweets_data = []


tweets_file = open(tweets_data_path, 'r')

for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except:
		continue

tweets_for_location = pd.DataFrame()
tweets_for_location["country"] = [tweet['place']['full_name'] for tweet in tweets_data if tweet['place']]
tweets_by_country = tweets_for_location["country"].value_counts()
#print tweets_by_country

fig,ax = plt.subplots()
ax.tick_params(axis = 'x', labelsize = 200)
ax.tick_params(axis = 'y', labelsize = 10)
ax.set_xlabel('places', fontsize = 15)
ax.set_xlabel('number of tweets', fontsize = 15)
ax.set_title('Location of the tweets', fontsize = 15, fontweight = 'bold')
tweets_by_country[:].plot(ax = ax, kind = 'bar', color = 'red')
plt.show()
