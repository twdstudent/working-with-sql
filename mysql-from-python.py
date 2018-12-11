import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if runnin on other enviroment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
                            
try:
    #Run a query
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        #note that the above will stil display a warning (not error) if the 
        #table already exists
finally:
    # close the connection. regardless of whether th eabove was succesfull
    connection.close()
    
    