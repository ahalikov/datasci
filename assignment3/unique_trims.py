"""
Assignment 3, Problem 5
Consider a set of key-value pairs where each key is sequence id and each 
value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....
Write a MapReduce query to remove the last 10 characters from each string of nucleotides, 
then remove any duplicates generated.
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
