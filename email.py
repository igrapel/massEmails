import win32com.client
import pyodbc 
import datetime
import bitdotio
import pandas as pd
from sqlalchemy import create_engine

outlook = win32com.client.Dispatch('outlook.application')

class Email:
    def __init__(self, subject, to, student, gender):
        self.mail = outlook.CreateItem(0)
        self.mail.To = to
        self.mail.Subject = subject
        self.mail.Body = ""
        self.gender = gender
        self.name = student
        self.time_stamp = datetime.datetime.now()
        #SQL Server
        self.conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TR5JF24\SQLEXPRESS;'
                      'Database=Contacts;'
                      'Trusted_Connection=yes;')

        self.cursor = self.conn.cursor()
        #bit io
        # Check out https://github.com/bitdotioinc/python-bitdotio for more examples and documentation
        self.client = bitdotio.bitdotio("QUch_FLetVVdmmBYmBT8v3B2hfp3")
        self.statement = ""
        self.PG_STRING = 'postgresql://igrapel_demo_db_connection:QWqR_9vmjf4dxRGqYcshquMKXWWX@db.bit.io'
       # print(self.client.list_repos())
        self.action = ""
    
    def send(self):
        if(self.gender == "Male"):
            adj = "his";
            obj = "him";
        elif(self.gender == "Female"):
            adj = "her";
            obj = "her";
        else:
            adj = "they";
            obj = "their";
        message = "Dear parents, " + "\n\nI am " + self.name + "'s computer science teacher. " +\
        self.name + " is not completing " + adj + " work. As a result, " +\
        self.name + " is in danger of failing the class. I hope you can speak with " + obj  + \
        " and encourage " + obj + " to put in the effort to pass the class.\n\n" +\
        "Sincerely, \n\nMr. Ilan Grapel\nIB and AP Computer Science \nCoral Gables Senior High";

        self.mail.Body = message
        self.mail.Send()
     
    def store_loc(self, statement, show = True):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-TR5JF24\SQLEXPRESS;'
                      'Database=Contacts;'
                      'Trusted_Connection=yes;')

        self.cursor = self.conn.cursor()
        self.cursor.execute(statement)
        self.conn.commit()
        if(show):
            self.cursor.execute('SELECT * FROM Parents')
        
    def store_ext(self, statement, action):
        self.action = action
        if(self.action == "change"):
            # Insert Values
            self.statement = statement
            with self.client.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(statement)

        elif(self.action =="retrieve"):
            # Return SQL query as a pandas dataframe
            # Create DF of data
            engine = create_engine(self.PG_STRING)
            with engine.connect() as conn:
                # Set 1 minute statement timeout (units are milliseconds)
                conn.execute("SET statement_timeout = 60000;")
                df = pd.read_sql(statement, conn)
                print(df.tail())
                
 #Run:
student = input("Student Name: ")
email = input("Email Name: ")
subject = input("Subject: ")  
gender = input("Male or Female: ")             
test = Email(subject, email, student, gender)
test.send()
test.store_loc("INSERT INTO Parents VALUES ('" + student+ "', '" + email+ "', " + "'" + str(test.time_stamp) +"'" + ", '" + subject + "', 'None');")
test.store_ext("INSERT INTO \"igrapel/Parents\".\"parents\" VALUES ('" + student + "', '" + email + "', '" + str(test.time_stamp) + "', '" + subject + "', '" + "None');", "change")
