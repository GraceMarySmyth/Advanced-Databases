def main():
    while True:
        display_menu()
        choice = input("Choice:")

        if (choice == 'x'):
            break
        elif (choice =="1"):
            View Directors_and_Films()
        else:
            print("Invalid choice, please try again.")

def display_menu():
    print("MoviesDB")
    print("---------")
    print("          ")
    print("MENU")
    print("====")
    print("1 - View Directors & Films")
    print("2 - View Actors by month of Birth")
    print("3 - Add New Actor")
    print("4 - View Married Actors")
    print("5 - Add Actor Marriage")
    print("6 - View Studios")
    print("x - Exit application")

def View_Directors_and_Films():
    search_name = input("Enter Director Name: ").lower()

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="moviesdb"
        )
        cursor = conn.cursor()

        query = """
            SELECT d.name, f.title, f.studio
            FROM directors d
            JOIN films f ON d.director_id = f.director_id
            WHERE LOWER(d.name) LIKE %s
        """
        cursor.execute(query, (f"%{search_name}%",))
        results = cursor.fetchall()

        if results:
            printed_directors = set()
            for director, title, studio in results:
                if director not in printed_directors:
                    print(f"\nFilm details for: {director}")
                    printed_directors.add(director)
                print(f"  - {title} (Studio: {studio})")
        else:
            print("No matching director found.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()