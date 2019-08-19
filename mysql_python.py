# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:25:35 2019

@author: Luna
"""

#!/usr/bin/python
import mysqldb
import mysql.connector    
db = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='movies_db')

# Create a Cursor object to execute queries.
cur = db.cursor()

# Select data from table using SQL query.
cur.execute("SELECT last_name FROM actors WHERE id<5")

for response in cur:
    print(response)
cur.close()
db.close()