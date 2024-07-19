import sqlite3 as sql

# Establishing database connection
con = sql.connect("data.db")
cur = con.cursor()

# Creating table for data storage
c1 = cur.execute("CREATE TABLE tags(tagname, priority)") 
c2 = cur.execute("CREATE TABLE timetrack(time, activity, tag)")

con.commit()
