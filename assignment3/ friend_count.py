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
    mr.emit_intermediate(record[0], record[1])

def reducer(key, list_of_values):
    count = 0
    for person in list_of_values:
        count += 1
    mr.emit((key, count))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
