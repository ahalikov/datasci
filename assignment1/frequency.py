"""
Assignment 1, problem 3: Term frequency
author: Artur Khalikov
"""

import sys
import json

clean = lambda s: s.replace(',', '').replace('.', '').replace('!', '').replace('#', '')

def increment(dic, term):
    dic[term] = dic[term] + 1.0 if term in dic else 1.0
    return dic
    
def main():
    tweet_file = open(sys.argv[1])
    file_occurences = {}
    tweets_occurences = []
    for line in tweet_file:
        json_data = json.loads(line)
        for key, value in json_data.items():
            if key == 'text':                
                terms = value.encode('utf-8').split()
                tweet_occurence = {}
                for term in terms:
                    file_occurences = increment(file_occurences, term)
                    tweet_occurence = increment(tweet_occurence, term)
                tweets_occurences.append(tweet_occurence)
    
    for terms in tweets_occurences:
        for term, value in terms.items():
            print '{0} {1:.3f}'.format(term, value / file_occurences[term])
                    
if __name__ == '__main__':
    main()
