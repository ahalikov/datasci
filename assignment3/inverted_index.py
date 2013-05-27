"""
Assignment 3, Problem 1
Create an Inverted index. 
Given a set of documents, an inverted index is a dictionary where each word is 
associated with a list of the document identifiers in which that word appears.
"""

__author__ = 'Artur Khalikov'

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = set(value.split())    
    for w in words:
        mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts    
    mr.emit((key, [d for d in list_of_values]))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
