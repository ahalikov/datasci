"""
Queries Twitter and prints out the text of each tweet in the result.
"""

import urllib
import json

def get_page(p):
    url = "http://search.twitter.com/search.json?q=microsoft&page={0}".format(p)    
    response = urllib.urlopen(url)
    json_response = json.load(response)
    return json_response['results']

for p in range(1,11):
    results = get_page(p)    
    for r in results:
        print(r['text'].encode('utf-8'))
        
