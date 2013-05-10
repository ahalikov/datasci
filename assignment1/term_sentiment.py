"""
Assignment 1, problem 3: Term Sentiment
author: Artur Khalikov
"""

import sys
import json

def load_scores(file_name):
    sent_file = open(file_name)
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores
    
def score_tweet(tweet, scores):
    terms = tweet.lower().split()
    score = 0
    for key, value in scores.items():
        occurences = terms.count(key)
        if occurences > 0:
            score += occurences * value
            terms.remove(key)
    return (score, terms)
        
def main():
    scores = load_scores(sys.argv[1])    
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        json_data = json.loads(line)
        for key, value in json_data.items():        
            if key == 'text':
                tweet = value.encode('utf-8')
                score = score_tweet(tweet, scores)
                for term in score[1]:
                    print '||{0}|| {1} {2:.3f}'.format(tweet, term, score[0])
                    #print '{0} {1:.3f}'.format(term, score[0])

if __name__ == '__main__':
    main()
