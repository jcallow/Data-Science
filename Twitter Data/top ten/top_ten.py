import sys
import json

def get_frequency(tweet):
	
	tweet_lines = tweet.readlines()
	
	my_list = []
	for line in tweet_lines:
		my_list.append(json.loads(line))
		
	tweet_entities = {}
	tweet_hashtags = {}
	hashtag_frequency = {}	
	for listk in my_list:
		if "entities" in listk:
			tweet_entities = listk["entities"]
			if "hashtags" in tweet_entities:
				 tweet_hashtags = tweet_entities["hashtags"]
				 for i in range(len(tweet_hashtags)):
					#print tweet_hashtags[i]['text']
					if tweet_hashtags[i]['text'] not in hashtag_frequency:
						hashtag_frequency[tweet_hashtags[i]['text']] = 1
					else:
						hashtag_frequency[tweet_hashtags[i]['text']] = hashtag_frequency[tweet_hashtags[i]['text']] + 1
	sorted_hashtags = []
	sorted_hashtags = sorted(hashtag_frequency, key=hashtag_frequency.get, reverse = True)
	for i in range(10):
		print "%s %s" % (sorted_hashtags[i], float(hashtag_frequency[sorted_hashtags[i]]))
	

	
def main():
	tweet_file = open(sys.argv[1])
	get_frequency(tweet_file)
	tweet_file.close()

if __name__ == '__main__':
    main()
