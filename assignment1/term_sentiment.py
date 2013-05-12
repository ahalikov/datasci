"""
Assignment 1, problem 3: Term Sentiment
"""

__author__ = 'Artur Khalikov'

import sys
import json

text = lambda tweet: tweet if 'text' in tweet else {}
lang_en = lambda tweet: tweet if 'lang' in tweet and tweet['lang'] == 'en' else {}
filters = lambda tweet: lang_en(text(tweet))

def load_scores(file_name):
    sent_file = open(file_name)
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def find(terms, key):
    if key not in terms:
        return False
    while key in terms:
        terms.remove(key)
    return True

"""
Score terms that are from AFINN-111.txt file
"""    
def score_known_terms(terms, scores):
    new_terms = {}
    score = 0
    for term in terms:
        term_lo = term.lower()
        if term_lo in scores:
            count = terms.count(term)
            score += (scores[term_lo]*1.0) / count
        else:
            new_terms[term] = 1
    return (score, new_terms, len(terms))

"""
Adjust score using
"""
def adjust_score(score, norm, terms, new_scores):
    # adjusting score
    for term in terms:
        if term in new_scores:
            t = new_scores[term]
            score += t[0]
    # assigning adjusted score to the new terms
    for term in terms:
        if term in new_scores:
            new_scores[term] = t
            value = (score*1.0) / (t[1] + 1)
            new_scores[term] = (value, t[1] + 1)
        else:
            value = (score*1.0) / norm                
            new_scores[term] = (value, 1)
    return score, new_scores

"""
Score a tweet
"""
def score_tweet(tweet, scores, new_scores):
    terms = [t.strip(',.!#') for t in tweet.split()]
    score, new_terms, norm = score_known_terms(terms, scores)
    score, new_scores = adjust_score(score, norm, new_terms, new_scores)
    return new_scores

"""
Score whole file
"""
def score_file(tweet_file, scores):
    new_scores = {}
    for line in tweet_file:
        tweet = filters(json.loads(line))
        if len(tweet) > 0:
            text = tweet['text'].encode('utf-8')
            new_scores = score_tweet(text, scores, new_scores)
    return new_scores
      
def main():
    scores = load_scores(sys.argv[1])    
    tweet_file = open(sys.argv[2])
    new_scores = score_file(tweet_file, scores)
    for term, score in new_scores.items():
        print('{0} {1:.3f}'.format(term, score[0]))

if __name__ == '__main__':
    main()
