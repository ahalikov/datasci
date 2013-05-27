"""
Assignment 3, Problem 6
Assume you have two matrices A and B in a sparse matrix format, 
where each record is of the form i, j, value.  
Design a MapReduce algorithm to compute matrix multiplication: A x B
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
