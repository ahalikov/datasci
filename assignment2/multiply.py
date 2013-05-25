"""
Assignment 2 problem 2: Matrix operations via sql
"""

__author__ = 'Artur Khalikov'

import sqlite3 as lite
import sys

con = None

def matrix_sum(cur):
    a = cur.execute("select row_num, col_num, aval + bval from ( \
            select a.row_num, a.col_num, \
            a.value aval, case when b.value is null then 0 else b.value end bval \
            from a left join b \
            on a.row_num = b.row_num and a.col_num = b.col_num)")
    for row in a:
        print(row)    
        
def matrix_mul(cur):
    a = cur.execute("select a.row_num, b.col_num, sum(a.value * b.value) \
        from a, b \
        where a.col_num = b.row_num \
        group by a.row_num, b.col_num")
    for row in a:
        print(row)

def main():
    try:
        con = lite.connect('matrix.db')        
        cur = con.cursor()
        matrix_mul(cur)
        
    except lite.Error, e:        
        print "Error %s:" % e.args[0]
        sys.exit(1)
        
    finally:        
        if con:
            con.close()        

if __name__ == '__main__':
    main()
