"""
Assignment 3, Problem 4
The relationship "friend" is often symmetric, 
meaning that if I am your friend, you are my friend. 
Implement a MapReduce algorithm to check whether this property holds. 
Generate a list of all non-symmetric friend relationships.
"""

__author__ = 'Artur Khalikov'

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate()

def reducer(key, list_of_values):
    mr.emit()

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
