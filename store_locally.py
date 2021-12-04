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
test = Local_Server()
test.send("INSERT INTO Parents VALUES ('Julio Leyva2', 'leyva.gmail.com', " + "'" + str(now) +"'" + ", 'Failure', 'None');")
