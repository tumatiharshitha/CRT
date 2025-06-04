import mysql.connector
def connect():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hari@2005",
        database="group_partner_matching_system"
    )
    return conn
if(connect()):
    print("Connection established successfully")
else:
    print("Connection failed")