#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_4_usa and their states
 Usage: ./0-select_states.py <mysql username> \
                             <mysql password> \
                             <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name` FROM `cities` INNER JOIN states ON `cities`.`state_id` = `states`.`id`")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
