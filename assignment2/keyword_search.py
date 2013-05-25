"""
Assignment 2 problem 4: Keyword Search
"""

__author__ = 'Artur Khalikov'

import sqlite3 as lite
import sys

con = None

def create_views(con):
    with con:
        cur = con.cursor()
        cur.executescript("""
            drop view if exists a;
            
            create view a as
            SELECT * FROM Frequency
            UNION
            SELECT 'q' as docid, 'washington' as term, 1 as count
            UNION
            SELECT 'q' as docid, 'taxes' as term, 1 as count
            UNION
            SELECT 'q' as docid, 'treasury' as term, 1 as count;            
           
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
            select * from (
                select a.docid, b.term, sum(a.count * b.count)
                from a, b
                where a.term = b.term
                group by a.docid, b.docid
            ) where docid = 'q'
            """)
        for row in rs:
            print(row)

def main():
    try:
        con = lite.connect(sys.argv[1])
        create_views(con)
        find_similarity(con)
        
    except lite.Error, e:        
        print "Error %s:" % e.args[0]
        sys.exit(1)
        
    finally:        
        if con:
            con.close()        

if __name__ == '__main__':
    main()
