"""
Assignment 1, problem 2: Tweet Sentiment
"""
__author__ = 'Artur Khalikov'

import sys
import json

def load_scores(file_name):
    sent_file = open(file_name)
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores
        
def load_tweets(file_name):
    tweet_file = open(file_name)
    tweets = []
    for line in tweet_file:
        json_data = json.loads(line)
        for key, value in json_data.items():        
            if key == 'text':
                tweets.append(value.encode('utf-8'))
    return tweets
    
def format_tweet(tweet):
    return tweet.replace(',', '').replace('.', '').replace('!', '')    
    
def score_tweet(tweet, scores):
    tweet_words = tweet.lower().split(' ')
    score = 0
    for key, value in scores.items():
        score += tweet_words.count(key) * value        
    return score
    
def pscore_tweet(tweet, scores):    
    tweet_words = tweet.lower().split(' ')
    score = 0
    sentiments = []
    for key, value in scores.items():
        if tweet_words.count(key) > 0:
            sentiments.append(key)
            score += tweet_words.count(key) * value        
    return '{0} {1:.2f}'.format(','.join(sentiments), score_tweet(tweet, scores))

def main():
    scores = load_scores(sys.argv[1])
    tweets = load_tweets(sys.argv[2])
    for tweet in tweets:
        score = pscore_tweet(format_tweet(tweet), scores)
        print('||{0}|| {1}'.format(tweet, score))

if __name__ == '__main__':
    main()
