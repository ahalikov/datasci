"""
Assignment 1, problem 3: Term frequency
author: Artur Khalikov
"""

import sys
import json

clean = lambda s: s.replace(',', '').replace('.', '').replace('!', '').replace('#', '')

def increment(dic, term):
    dic[term] = dic[term] + 1 if term in dic else 1
    return dic
    
def main():
    tweet_file = open(sys.argv[1])
    file_occurences = {}
    for line in tweet_file:
        json_data = json.loads(line)
        for key, value in json_data.items():
            if key == 'text':                
                terms = value.encode('utf-8').split()
                for term in terms:
                    file_occurences = increment(file_occurences, term)
    total = 0
    for term, value in file_occurences.items():
        total += value
    
    for term, value in file_occurences.items():
        print '{0} {1:.3f}'.format(term, (value * 1.0) / total)
                    
if __name__ == '__main__':
    main()
