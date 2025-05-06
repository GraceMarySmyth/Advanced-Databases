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

def add_Actor(ActorID, ActorName, ActorDOB, ActorGender, ActorCountryID):
    global conn
    if not conn:
        connect()
       
    try:
        # Check if the actor already exists
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM actor WHERE ActorID = %s", (ActorID,))
            if cursor.fetchone():
                print("***ERROR*** Actor ID already exists.")
                return
            
            # Check if the country ID exists
            cursor.execute("SELECT * FROM country WHERE CountryID = %s", (ActorCountryID,))
            if not cursor.fetchone():
                print("***ERROR*** country ID does not exist.")
                return
            
            # Insert the new actor
            query = "INSERT INTO actor(ActorID, ActorName, ActorDOB, ActorGender, ActorCountryID) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (ActorID, ActorName, ActorDOB, ActorGender, ActorCountryID))
            conn.commit()
            print("Actor successfully added. Returning to main menu.")
    
    except pymysql.MySQLError as e:
        print(f"***ERROR*** {e}")

    except Exception as e:
        print(f"***ERROR*** {e}")
    

