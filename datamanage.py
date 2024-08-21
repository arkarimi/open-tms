
# Creating data managing tools for ease of access

import datetime
import sqlite3


class Data:
    def __init__(self):
        pass

    
    def todayTableName(self):
        timex =datetime.datetime.now()
        today = f'rec_{timex.year}_{timex.month}_{timex.day}'

        return today

    def checktodayexists(self):
        timex =datetime.datetime.now()
        exists = 0
        today = f'rec_{timex.year}_{timex.month}_{timex.day}'

        con = sqlite3.connect('data.db')
        cur = con.cursor()

        cmd1 = f"SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        cur.execute(cmd1)

        tables = cur.fetchall()

        con.commit()
        con.close()

        for table in tables:
            if table[0] == today:
                exists = 1







        return exists
    
    def checkotherdayexists(recordname):
        
        exists = 0
        today = recordname

        con = sqlite3.connect('data.db')
        cur = con.cursor()

        cmd1 = f"SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        cur.execute(cmd1)

        tables = cur.fetchall()

        con.commit()
        con.close()

        for table in tables:
            if table[0] == today:
                exists = 1


        return exists

    def addDay(self,timex =datetime.datetime.now()):
        
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        cmd1 = f'CREATE TABLE rec_{timex.year}_{timex.month}_{timex.day} (starttime, endtime, activity, tag, priority)'
        cur.execute(cmd1)
            


        con.commit()
        con.close()

    def addtable(self, name):
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        cmd1 = f'CREATE TABLE {name} (starttime, endtime, activity, tag, priority)'
        cur.execute(cmd1)
            


        con.commit()
        con.close()

    def getdaydata(self, date):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        cursor.execute(f'SELECT * FROM {date}')
        daydata = cursor.fetchall()
        conn.close()

        return daydata


d = Data()
d.checktodayexists()