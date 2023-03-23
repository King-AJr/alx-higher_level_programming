#!/usr/bin/python3
"""
display all values in the states where name matches an arguent
 Usage: ./1-filter_states.py <mysql username> \
                             <mysql password> \
                             <database name>
                              <state name searched>   
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    state = sys.argv[4]
    query = "SELECT * FROM states WHERE name = %s"
    cur.execute(query, (state,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
