__author__ = 'Artur'

import sys
import json

ENCODE_TEXT = True

"""
Returns a list of tweet terms
"""
def get_terms(tweet, encode=True):
    text = tweet['text'].encode('utf-8') if encode else tweet['text']
    return text.split()

def get_hash_tags(tweet_file):
    has_text = lambda tweet: tweet if 'text' in tweet else {}
    apply_filters = lambda tweet: has_text(tweet)

    tags = {}
    for line in tweet_file:
        tweet = apply_filters(json.loads(line))
        if len(tweet) > 0:
            terms = get_terms(tweet, ENCODE_TEXT)
    return tags

def get_top_tags(tags):
    return tags

def main():
    tweet_file = open(sys.argv[1])
    tags = get_top_tags(get_hash_tags(tweet_file))
    for tag in tags:
        print(tag)

if __name__ == '__main__':
    main()
