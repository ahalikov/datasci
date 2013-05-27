"""
Assignment 3, Problem 3
Consider a simple social network dataset consisting of key-value pairs 
    where each key is a person and each value is a friend of that person. 
Describe a MapReduce algorithm to count he number of friends each person has.
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
