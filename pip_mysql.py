# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:08:58 2019

@author: Luna
"""

import pip
from pip._internal import main
main(['install','mysql-connector-python-rf'])

import mysql.connector



db = mysql.connector.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="",     # password
                     db="movies_db")   # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()

# Select data from table using SQL query.
cur.execute("SELECT last_name FROM actors WHERE last_name LIKE '%K%'")
for response in cur :
    print(response)