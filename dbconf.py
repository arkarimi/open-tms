import sqlite3 as sql

# Establishing database connection
con = sql.connect("data.db")
cur = con.cursor()

# Creating table for data storage
c1 = cur.execute("CREATE TABLE settings(option, state)")
c1 = cur.execute("CREATE TABLE tags(tagname, priority)")
con.commit()
