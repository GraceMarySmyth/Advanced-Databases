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

def view_actor(month_input):
    global conn
    if not conn:
        connect()

    month_map = {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
        "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
    }

    if month_input.isdigit():
        month = int(month_input)
    else:
        month = month_input.lower()
        month = month_map.get(month_input.lower()[:3], 0)

    if not (1 <= month <= 12):
        print("Invalid month.")
        return None

    query = "SELECT ActorName, ActorDOB, ActorGender FROM actor WHERE MONTH(ActorDOB) = %s"
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (month,))
            return cursor.fetchall()
    except Exception as e:
        print("Database error:", e)
        return None