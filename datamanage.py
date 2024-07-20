
# Creating data managing tools for ease of access

import datetime
import sqlite3


class Data:
    def __init__(self):
        pass

    def addDay(self,timex =datetime.datetime.now()):
        
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        cmd1 = f'CREATE TABLE rec_{timex.year}_{timex.month}_{timex.day} (starttime, endtime, activity, tag, priority)'
        cur.execute(cmd1)
            


        con.commit()
        con.close()

