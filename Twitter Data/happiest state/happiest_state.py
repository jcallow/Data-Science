import sys
import json

def state_to_code_dic():
	state_to_code = {
					"VERMONT": "VT",
					"GEORGIA": "GA",
					"IOWA": "IA", 
					"Armed Forces Pacific": "AP", 
					"GUAM": "GU", 
					"KANSAS": "KS", 
					"FLORIDA": "FL", 
					"AMERICAN SAMOA": "AS", 
					"NORTH CAROLINA": "NC", 
					"HAWAII": "HI", 
					"NEW YORK": "NY", 
					"CALIFORNIA": "CA", 
					"ALABAMA": "AL", 
					"IDAHO": "ID", 
					"FEDERATED STATES OF MICRONESIA": "FM", 
					"Armed Forces Americas": "AA", 
					"DELAWARE": "DE", 
					"ALASKA": "AK", 
					"ILLINOIS": "IL", 
					"Armed Forces Africa": "AE", 
					"SOUTH DAKOTA": "SD", 
					"CONNECTICUT": "CT", 
					"MONTANA": "MT", 
					"MASSACHUSETTS": "MA", 
					"PUERTO RICO": "PR", 
					"Armed Forces Canada": "AE", 
					"NEW HAMPSHIRE": "NH", 
					"MARYLAND": "MD", 
					"NEW MEXICO": "NM", 
					"MISSISSIPPI": "MS", 
					"TENNESSEE": "TN", 
					"PALAU": "PW", "COLORADO": "CO", 
					"Armed Forces Middle East": "AE", 
					"NEW JERSEY": "NJ", 
					"UTAH": "UT", 
					"MICHIGAN": "MI", 
					"WEST VIRGINIA": "WV", 
					"WASHINGTON": "WA", 
					"MINNESOTA": "MN", 
					"OREGON": "OR", 
					"VIRGINIA": "VA", 
					"VIRGIN ISLANDS": "VI", 
					"MARSHALL ISLANDS": "MH", 
					"WYOMING": "WY", 
					"OHIO": "OH", 
					"SOUTH CAROLINA": "SC", 
					"INDIANA": "IN", 
					"NEVADA": "NV", 
					"LOUISIANA": "LA", 
					"NORTHERN MARIANA ISLANDS": "MP", 
					"NEBRASKA": "NE", 
					"ARIZONA": "AZ", 
					"WISCONSIN": "WI", 
					"NORTH DAKOTA": "ND", 
					"Armed Forces Europe": "AE", 
					"PENNSYLVANIA": "PA", 
					"OKLAHOMA": "OK", 
					"KENTUCKY": "KY", 
					"RHODE ISLAND": "RI", 
					"DISTRICT OF COLUMBIA": "DC", 
					"ARKANSAS": "AR", 
					"MISSOURI": "MO", 
					"TEXAS": "TX", 
					"MAINE": "ME"
	}
	return state_to_code

def state_sentiment_dic():
	states = {
        'AK': 0,
        'AL': 0,
        'AR': 0,
        'AS': 0,
        'AZ': 0,
        'CA': 0,
        'CO': 0,
        'CT': 0,
        'DC': 0,
        'DE': 0,
        'FL': 0,
        'GA': 0,
        'GU': 0,
        'HI': 0,
        'IA': 0,
        'ID': 0,
        'IL': 0,
        'IN': 0,
        'KS': 0,
        'KY': 0,
        'LA': 0,
        'MA': 0,
        'MD': 0,
        'ME': 0,
        'MI': 0,
        'MN': 0,
        'MO': 0,
        'MP': 0,
        'MS': 0,
        'MT': 0,
        'NA': 0,
        'NC': 0,
        'ND': 0,
        'NE': 0,
        'NH': 0,
        'NJ': 0,
        'NM': 0,
        'NV': 0,
        'NY': 0,
        'OH': 0,
        'OK': 0,
        'OR': 0,
        'PA': 0,
        'PR': 0,
        'RI': 0,
        'SC': 0,
        'SD': 0,
        'TN': 0,
        'TX': 0,
        'UT': 0,
        'VA': 0,
        'VI': 0,
        'VT': 0,
        'WA': 0,
        'WI': 0,
        'WV': 0,
        'WY': 0
	}
	return states

def get_average(num, sentiment):
	for key in sentiment:
		if num[key] != 0:
			sentiment[key] = sentiment[key]/float(num[key])
	return sentiment

def get_max(dic):
	maximum = float("-infinity")
	maximum_key = ""
	for key in dic:
		if dic[key] >  maximum:
			maximum = dic[key]
			maximum_key = key
	return maximum_key

def get_sentiment(key, scores):
	tweet_value = 0
	if "text" in key:
		tweet_text = key["text"]
		tweet_words = tweet_text.split()
		for word in tweet_words:
			if word in scores:
				tweet_value = tweet_value + scores[word]
	return tweet_value
	
def hw(sentiment, tweet):
	state_to_code = state_to_code_dic()
	states_sentiment = state_sentiment_dic()
	states_tweetnum = state_sentiment_dic()
	
	scores = {}
	for line in sentiment:
		term, score = line.split("\t")
		scores[term] = int(score)
	
	tweet_lines = tweet.readlines()
	
	my_list = []
	for line in tweet_lines:
		my_list.append(json.loads(line))
	
	for listk in my_list:
		if "place" in listk:
			if listk['place'] != None:
				if listk['place']['country_code'] == 'US':
					for state in listk['place']["full_name"].split(', '):
						if state in states_sentiment:
							states_sentiment[state] = states_sentiment[state]+get_sentiment(listk, scores)
							states_tweetnum[state] = states_tweetnum[state]+1
						elif state in state_to_code:
							states_sentiment[state_to_code[state]] = states_sentiment[state_to_code[state]] + get_sentiment(listk, scores)
							states_tweetnum[state_to_code[state]] = states_tweetnum[state_to_code[state]]+1
		
	states_sentiment = get_average(states_tweetnum, states_sentiment)
	print get_max(states_sentiment)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    state_to_code_dic()
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
