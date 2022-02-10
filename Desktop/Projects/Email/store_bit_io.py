# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 00:07:11 2021

@author: ilang
"""


import bitdotio
import time

import pandas as pd
from sqlalchemy import create_engine


class External_Server():
    def __init__(self):
        # Check out https://github.com/bitdotioinc/python-bitdotio for more examples and documentation
        self.client = bitdotio.bitdotio("QUch_FLetVVdmmBYmBT8v3B2hfp3")
        self.statement = ""
        self.PG_STRING = 'postgresql://igrapel_demo_db_connection:QWqR_9vmjf4dxRGqYcshquMKXWWX@db.bit.io'
       # print(self.client.list_repos())
        self.action = ""

    def send(self, statement, action):
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
                df = pd.read_sql(sql, conn)
                print(df.tail(10))
                   
# Delete Values if necessary
delete_sql = """
DELETE FROM "igrapel/Parents"."parents" WHERE date = '2022-01-18T19:30:55.072'
"""

# Insert Values
insert_sql = """
    INSERT INTO "igrapel/Parents"."parents" VALUES ('Daniel Ramirez', 'Student Email', '2022-01-04 21:15:02.8044680', 'Zoom Link', 'Covid');
    """

update_sql = """
    UPDATE "igrapel/Parents"."parents" SET response = 'Mother claims son completed work. Will check.' WHERE "igrapel/Parents"."parents"."contact" LIKE '%anareginam@yahoo.com%';
    """
    
# Define your username and PostgreSQL connection string here
USERNAME = 'igrapel_demo_db_connection'



# SQL for querying an entire table
sql = '''
    SELECT *
    FROM "igrapel/Parents"."parents";
'''

  
test = External_Server()
test.send (update_sql, "change")
test.send(sql, "retrieve")

  
  
  