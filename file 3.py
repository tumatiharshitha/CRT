import mysql.connector
def connection():
    conn=mysql.connector.connect(

        host="localhost",
        user="root",
        password="root",
        database="student_management3"

    )
    return conn
if(connection()):
    print("connection established successfully")
else:
    print("connection faild")