"""
Assignment 3, Problem 2
Implement a relational join as a MapReduce query.
"""

__author__ = 'Artur Khalikov'

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: table name    
    key = record[0]
    # order_id 
    order_id = record[1]
    values = record[2:]    
    mr.emit_intermediate(order_id, (key, values))

def reducer(key, list_of_values):
    # key: order_id
    # order
    order = list_of_values[0]
    join = [order[0], key] + order[1]
    # line_item(s)
    for t in list_of_values[1:]:
        mr.emit(join + [t[0], key] + t[1])

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
