import sys
import json

def get_frequency(tweet):
	tweet_lines = tweet.readlines()
	
	my_list = []
	for line in tweet_lines:
		my_list.append(json.loads(line))
		
	new_words = {}	
	for listk in my_list:
		if "text" in listk:
			tweet_text = listk["text"]
			tweet_words = tweet_text.split()
			for word in tweet_words:
				if word not in new_words:
					new_words[word] = 1
				else:
					new_words[word] = new_words[word] + 1
					
	for new_word in new_words:
		print "%s %s" % (new_word, new_words[new_word])
	
def main():
	tweet_file = open(sys.argv[1])
	get_frequency(tweet_file)

if __name__ == '__main__':
    main()
