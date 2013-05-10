"""
Assignment 1, problem 4: Happiest state
author: Artur Khalikov
"""

import sys
import json

def us(tweet):
    if 'place' not in tweet or tweet['place'] is None:
        return {}
    place = tweet['place']
    return tweet if 'country_code' in place and place['country_code'] == 'US' else {}            
    
text = lambda tweet: tweet if 'text' in tweet else {}
filters = lambda tweet: us(text(tweet))

def load_scores(file_name):
    sent_file = open(file_name)
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores
    
def main():
    scores = load_scores(sys.argv[1])
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweet = filters(json.loads(line))
        if len(tweet) > 0:
            #

if __name__ == '__main__':
    main()

