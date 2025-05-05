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

    query = "SELECT d.DirectorName, f.FilmName, s.StudioName FROM director d JOIN film f ON d.DirectorID = f.FilmDirectorID JOIN studio s ON f.FilmStudioID = s.StudioID WHERE d.DirectorName LIKE %s"

    with conn.cursor() as cursor:
        cursor.execute(query, ('%' + name + '%',))
        x = cursor.fetchall()
        if not x:
            print("No directors found of that name")
            return None
        return x
       