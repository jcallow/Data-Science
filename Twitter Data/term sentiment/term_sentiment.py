import sys
import json

def hw(sentiment, tweet):
	scores = {}
	for line in sentiment:
		term, score = line.split("\t")
		scores[term] = int(score)
	
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
				if (word not in scores) and (word not in new_words):
					new_words[word] = 0
	
	for listk in my_list:
		if "text" in listk:
			tweet_text = listk["text"]
			tweet_words = tweet_text.split()
			for word in tweet_words:
				if word in scores:
					for new_word in tweet_words:
						if new_word not in scores:
							new_words[new_word] = new_words[new_word] + scores[word]
	

	for new_word in new_words:
		print "%s %s" % (new_word, new_words[new_word])
	
	
	

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
