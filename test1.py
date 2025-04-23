import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    username="root2",
    password="Pass@1234"
    
)
if conn.is_connected():
    print("connected")