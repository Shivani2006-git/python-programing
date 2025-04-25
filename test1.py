import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    username="root2",
    password="Pass@1234",
    database="goal"
    
)
mycursor=conn.cursor()

mycursor.execute("show tables")

for i in mycursor:
    print(i)