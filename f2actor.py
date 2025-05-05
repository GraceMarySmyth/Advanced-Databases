import pymysql

conn = None

def connect():
    global conn
    conn = pymysql.connect(
        host="localhost", 
        user="root", 
        password="root", 
        db="appdbproj", 
        cursorclass=pymysql.cursors.DictCursor
        )

def view_director(name):
    global conn
    if not conn:
        connect()

query = "select ActorName, ActorDOB, ActorGender FROM actor; WHERE MONTH(actorDOB) = 2"

    with conn.cursor() as cursor:
        cursor.execute(query, (1<= month >=12,))
        x = cursor.fetchall()
        if not x:
            print("No actors born that month.")
            return None
        return x 