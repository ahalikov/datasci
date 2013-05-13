__author__ = 'Artur'

import sys
import json

encode_text = False

def get_hashtags(tweet_file):
    hashtags = {}
    for line in tweet_file:
        tweet = json.loads(line)
        if 'entities' in tweet:
            if 'hashtags' in tweet['entities']:
                if len(tweet['entities']['hashtags']) > 0:
                    for tag in tweet['entities']['hashtags']:
                        text = tag['text']
                        hashtags[text] = hashtags[text] + 1 if text in hashtags else 1
    return hashtags

def get_top_ten(tags):
    tags = dict((key, tags[key]) for key in sorted(tags, key=tags.get))
    return tags if len(tags) <= 10 else dict(tags.popitem() for i in range(10))

def main():
    tweet_file = open(sys.argv[1])
    tags = get_top_ten(get_hashtags(tweet_file))
    for tag, count in tags.items():
        print('{0} {1:.2f}'.format(tag, count))

if __name__ == '__main__':
    main()
