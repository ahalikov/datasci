__author__ = 'Artur'

import sys
import json

encode_text = False

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
            terms = get_terms(tweet, encode_text)
            for term in terms:
                if term.count('#') > 0:
                    tags[term] = tags[term] + 1 if term in tags else 1
    return tags

def get_top_tags(tags):
    tags = dict((key, tags[key]) for key in sorted(tags, key=tags.get))
    return tags if len(tags) <= 10 else dict(tags.popitem() for i in range(10))

def main():
    tweet_file = open(sys.argv[1])
    tags = get_top_tags(get_hash_tags(tweet_file))
    for tag, count in tags.items():
        print('{0} {1:.2f}'.format(tag, count))

if __name__ == '__main__':
    main()
