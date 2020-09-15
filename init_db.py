# Import MySQL Connector Driver
import mysql.connector as mysql

from datetime import datetime

# Load the credentials from the secured .env file
import os
from dotenv import load_dotenv
load_dotenv('credentials.env')

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST'] # must 'localhost' when running this script outside of Docker
#db_host = 'localhost'

# Connect to the database
db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
cursor.execute("drop table if exists TStudents;")
cursor.execute("drop table if exists Tcuser;")
cursor.execute("drop table if exists Moves;")
cursor.execute("drop table if exists Customers;")
cursor.execute("drop table if exists News;")
cursor.execute("drop table if exists Users;")
cursor.execute("drop table if exists visits;")
  
# Create a Customerss table (wrapping it in a try-except is good practice)
try:
  cursor.execute("""
    CREATE TABLE Customers (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      first_name  VARCHAR(30),
      last_name   VARCHAR(30),
      email       VARCHAR(50),
      phonenumber VARCHAR(20),
      password    VARCHAR(20),
      created_at  TIMESTAMP
    );
  """)
except:
  print("Users table already exists. Not recreating it.")
  
try:
  cursor.execute("""
    CREATE TABLE News (
      id integer  AUTO_INCREMENT PRIMARY KEY,
      title VARCHAR(130) NOT NULL,
      time VARCHAR(130) NOT NULL,
      content VARCHAR(130) NOT NULL
    );
  """)
except:
  print("Table already exists. Not recreating it.")
  
try:
  cursor.execute("""
    CREATE TABLE visits (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      session_id  VARCHAR(30) NOT NULL,
      route_name   VARCHAR(30) NOT NULL,
      previous_has_signed_in   integer NOT NULL,
      timestamp  TIMESTAMP
    );
  """)
except:
  print("visits table already exists. Not recreating it.")

# Insert Records
query = "insert into Customers (first_name, last_name, email, phonenumber, password, created_at) values (%s, %s, %s, %s, %s, %s)"
values = [
  ('ramsin', 'khoshabeh', 'ramsin@khoshabeh.com', '111-111-1111', 'abc123', datetime.now()),
  ('David', 'He', 'dyhe@ucsd.edu', '111-111-1111', 'abc123', datetime.now())
]
cursor.executemany(query, values)
db.commit()

query = "insert into News (title, time, content) values (%s, %s, %s)"
values = [
  ('Suro Bathroom Fixtures is now open in business','9/14/2020','Do not get too excited')
]
cursor.executemany(query, values)
db.commit()

# Selecting Records
cursor.execute("select * from Customers;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]
db.close()
