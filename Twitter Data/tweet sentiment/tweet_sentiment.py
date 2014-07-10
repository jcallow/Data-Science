import sys
import json

def hw(sentiment, tweet):
	scores = {}
	for line in sentiment:
		term, score = line.split("\t")
		scores[term] = int(score)
	#print scores.items()
	
	tweet_lines = tweet.readlines()
	
	my_list = []
	for line in tweet_lines:
		my_list.append(json.loads(line))
		
	for listk in my_list:
		tweet_value = 0
		if "text" in listk:
			tweet_text = listk["text"]
			tweet_words = tweet_text.split()
			for word in tweet_words:
				if word in scores:
					tweet_value = tweet_value + scores[word]
		print tweet_value


def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
   # lines(sent_file)
   # lines(tweet_file)
    sent_file.close()
    tweet_file.close()

if __name__ == '__main__':
    main()
