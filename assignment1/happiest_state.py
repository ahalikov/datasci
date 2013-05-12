"""
Assignment 1, problem 4: Happiest state
"""

__author__ = 'Artur'

import sys
import json

"""
US States dictionary
"""
us_states = {
    'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AS': 'American Samoa', 'AZ': 'Arizona', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DC': 'District of Columbia', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'GU': 'Guam', 'HI': 'Hawaii', 'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas',
    'KY': 'Kentucky', 'LA': 'Louisiana', 'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine', 'MI': 'Michigan',
    'MN': 'Minnesota', 'MO': 'Missouri', 'MP': 'Northern Mariana Islands', 'MS': 'Mississippi', 'MT': 'Montana', 'NA': 'National',
    'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico',
    'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'PR': 'Puerto Rico',
    'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
    'VA': 'Virginia', 'VI': 'Virgin Islands', 'VT': 'Vermont', 'WA': 'Washington', 'WI': 'Wisconsin', 'WV': 'West Virginia',
    'WY': 'Wyoming'
}

def form_us(tweet):
    if 'place' not in tweet or tweet['place'] is None:
        return {}
    place = tweet['place']
    return tweet if 'country_code' in place and place['country_code'] == 'US' else {}            
    
has_text = lambda tweet: tweet if 'text' in tweet else {}
lang_en = lambda tweet: tweet if 'lang' in tweet and tweet['lang'] == 'en' else {}
apply_filters = lambda tweet: lang_en(form_us(has_text(tweet)))

"""
Returns tweet's user location
"""
def get_user_location(tweet):
    if 'user' not in tweet:
        return ''
    return tweet['user']['location'] if 'location' in tweet['user'] else ''

def get_place_name(tweet):
    return tweet['place']['full_name'] if 'full_name' in tweet['place'] else ''

"""
Loads score database AFINN-111
"""
def load_scores(file_name):
    sent_file = open(file_name)
    scores = {}
    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = int(score)
    return scores

"""
Give a tweet score
"""
def score_tweet(terms, scores):
    score = 0
    for term in terms:
        term_lo = term.lower()
        if term_lo in scores:
            count = terms.count(term)
            score += (scores[term_lo] * 1.0) / count
    return score

def get_state(tweet):
    def lookup(place):
        if len(place) > 0:
            for t in place:
                if t in us_states:
                    return t;
        return ''
    # Trying to define state from user data
    state = lookup(get_user_location(tweet).split())
    if state == '':
        # Trying to define state from place
        state = lookup(get_place_name(tweet).split())
    return state
    
def main():
    scores = load_scores(sys.argv[1])
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweet = apply_filters(json.loads(line))
        if len(tweet) > 0:
            state = get_state(tweet)
            location = get_user_location(tweet)
            print('state={0}, location={1}'.format(state, location))
            print(us_states['CA'])
            #text = tweet['text'].encode('utf-8')
            #terms = [t.strip(',.!#') for t in text.split()]

if __name__ == '__main__':
    main()