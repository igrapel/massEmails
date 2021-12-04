# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 13:58:47 2021

@author: ilang
"""

import bitdotio
import csv
from io import StringIO
import time

import pandas as pd
from sqlalchemy import create_engine


# Check out https://github.com/bitdotioinc/python-bitdotio for more examples and documentation
client = bitdotio.bitdotio("QUch_FLetVVdmmBYmBT8v3B2hfp3")
print(client.list_repos())


# Insert Values
insert_sql = """
    INSERT INTO "igrapel/Parents"."parents" VALUES ('Julio Leyva2', 'leyva.gmail.com', '2021-11-1T22:12:23', 'Failure', 'None');
    """
# Delete Values if necessary
delete_sql = """
DELETE FROM "igrapel/Parents"."parents" WHERE date = '2021-11-01 22:12:23'
"""
with client.get_connection() as conn:
    cursor = conn.cursor()
    cursor.execute(insert_sql)
    
with client.get_connection() as conn:
    cursor = conn.cursor()
    cursor.execute(delete_sql)

# Define your username and PostgreSQL connection string here
USERNAME = 'igrapel_demo_db_connection'
PG_STRING = 'postgresql://igrapel_demo_db_connection:QWqR_9vmjf4dxRGqYcshquMKXWWX@db.bit.io'

# Create DF of data
engine = create_engine(PG_STRING)
# SQL for querying an entire table
sql = '''
    SELECT *
    FROM "igrapel/Parents"."parents";
'''
# Return SQL query as a pandas dataframe
with engine.connect() as conn:
    # Set 1 minute statement timeout (units are milliseconds)
  conn.execute("SET statement_timeout = 60000;")
  df = pd.read_sql(sql, conn)
  print(df.tail())
