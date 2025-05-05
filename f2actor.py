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

def view_actor_by_month(name):
    global conn
    if not conn:
        connect()

query = "SELECT ActorName, ActorDOB, ActorGender FROM actor WHERE MONTH(ActorDOB) = %s"

while True:
    try:
        month = int(input("Enter a month (1-12): "))
        if 1 <= month <= 12:
            break
        else:
            print("Please enter a valid month between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 12.")

with conn.cursor() as cursor:
    cursor.execute(query, (month,))
    x = cursor.fetchall()
    if not x:
        print("No actors born that month.")
        return None
    return x