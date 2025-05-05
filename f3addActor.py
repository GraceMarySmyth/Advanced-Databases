import pymysql

def connect():
    global conn
    conn = pymysql.connect(
        host="localhost", 
        user="root", 
        password="root", 
        db="appdbproj", 
        cursorclass=pymysql.cursors.DictCursor
        )

def add_Actor(ActorID, ActorName, ActorDOB, ActorGender, ActorCountryID):
    global conn
    if not conn:
        connect()
        
    query = "INSERT INTO actor(ActorID, ActorName, ActorDOB, ActorGender, CountryID)"
    
    with conn.cursor() as cursor:
        cursor.execute(query + " VALUES (%s, %s, %s, %s, %s)", (ActorID, ActorName, ActorDOB, ActorGender, ActorCountryID))
        x = cursor.fetchall()
        print("Actor successfully added. Returning to the main menu.")
        return x 