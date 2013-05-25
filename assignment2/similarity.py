"""
Assignment 2 problem 3: Similarity matrix
"""

__author__ = 'Artur Khalikov'

import sqlite3 as lite
import sys

"""
Creates two views a, b 
that represent matrix and transposed matrix
"""
def create_views(con):
    with con:
        cur = con.cursor()
        cur.executescript("""
            drop view if exists a;
            create view a
            as select * from Frequency
            where docid in ('10080_txt_crude', '17035_txt_earn');
            
            drop view if exists b;
            create view b as select term, docid, count from a;
            """)

"""
Matrix product (similarity matrix)
    a = ||docid||term ||count||
    b = ||term ||docid||count||
"""       
def find_similarity(con):
    with con:
        cur = con.cursor()
        rs = cur.execute("""
            select a.docid, b.term, sum(a.count * b.count)
            from a, b
            where a.term = b.term and a.docid < b.docid
            group by a.docid, b.docid
            """)
        for row in rs:
            print(row)

def main():
    try:        
        con = lite.connect(sys.argv[1])
        create_views(con)
        find_similarity(con)
        
    except lite.Error as e:
        print('Error {0}: '.format(e.args[0]))
        sys.exit(1)
        
    finally:        
        if con:
            con.close()        

if __name__ == '__main__':
    main()
