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

    month_map = {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
        "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
    }

    while True:
        try:
            month = input("Enter a month (1-12 or first three letters): ").strip().lower()
            if user_input.isdigit():
                month = int(user_input)
            if 1 <= month <= 12:
                break
            else:
                print("Please enter a valid month between 1 and 12.")
        elif user_input in month_map:
            month = month_map[user_input]
            break
        else:
            print("Invalid input. Please enter a number between 1 and 12 or the first three letters of a month.")

    with conn.cursor() as cursor:
        cursor.execute(query, (month,))
        x = cursor.fetchall()
        if not x:
            print("No actors born that month.")
            return None
        return x