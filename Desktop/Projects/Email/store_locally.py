# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 21:41:39 2021

@author: ilang
"""

import pyodbc 
import datetime



now = datetime.datetime.now()

class Local_Server():
    def __init__(self):
        self.time_stamp = datetime.datetime.now()
        self.conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TR5JF24\SQLEXPRESS;'
                      'Database=Contacts;'
                      'Trusted_Connection=yes;')

        self.cursor = self.conn.cursor()

    def send(self,statement, show = True):
        self.cursor.execute(statement)
        self.conn.commit()
        if(show):
            self.cursor.execute('SELECT * FROM Parents')

'''
cursor.execute("INSERT INTO Parents VALUES ('Julio Leyva2', 'leyva.gmail.com', " + "'" + str(now) +"'" + ", 'Failure', 'None');")
conn.commit()
cursor.execute('SELECT * FROM Parents')

for i in cursor:
    print(i)
    

'''
ins_sql = ("INSERT INTO Parents VALUES ('Daniel Ramirez', 'From student', " + "'" + str(now) +"'" + ", 'Covid', 'Covid');")
comment = input("Comment: ")
address = input("Email Address: ")
update_sql = "UPDATE Parents SET Comment = '" + comment + "' WHERE email LIKE '%" + address + "%'"
test = Local_Server()
test.send(update_sql)
#UPDATE "igrapel/Parents"."parents" SET "comment" = 'will speak with student'
#WHERE contact LIKE '%vaniacampos79@gmail.com%';
