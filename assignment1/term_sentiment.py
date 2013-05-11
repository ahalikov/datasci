"""
Assignment 1, problem 3: Term Sentiment
author: Artur Khalikov
"""

import sys
import json

new_scores = {}
text = lambda tweet: tweet if 'text' in tweet else {}
filters = lambda tweet: text(tweet)

def load_scores(file_name):
    sent_file = open(file_name)
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def add_term(term, score):
    score = new_scores[term] + score if term in new_scores else score
    new_scores[term] = (score, 1)
    
def find(terms, key):
    terms_lo = [t for t in terms]
    count = terms_lo.count(key)
    if count > 0:
        for t, tlo in zip(terms, terms_lo):
            if tlo == key:
                terms.remove(t)
    return count
    
def score_tweet(tweet, scores):
    terms = tweet.split()
    score = 0.0
    for key, value in scores.items():        
        occurences = find(terms, key)        
        if occurences > 0:
            score += value    
    for term in terms:
        if term in new_scores:            
            score += new_scores[term][0]
    for term in terms:
        if term in new_scores:
            t = new_scores[term]
            new_scores[term] = (score, t[1] + 1)
        else:
            add_term(term, score)
    return score        
        
def main():
    scores = load_scores(sys.argv[1])    
    tweet_file = open(sys.argv[2])
    
    for line in tweet_file:
        tweet = filters(json.loads(line))
        if len(tweet) > 0:
            text = tweet['text'].encode('utf-8')
            score = score_tweet(text, scores)
            #print '{0} || {1}'.format(text, score)
    
    for term, score in new_scores.items():
        print '{0} {1:.3f}'.format(term, score[0] / score[1])

if __name__ == '__main__':
    main()
