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

def view_studio():
    global conn
    if not conn:
        connect()
        
    query = "SELECT StudioID, StudioName FROM studio ORDER BY StudioID"

    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            x = cursor.fetchall()
            if not x:
                print("No studios found")
                return None
            return x
    except Exception as e:
        print("Error fetching studios:", e)
        return None