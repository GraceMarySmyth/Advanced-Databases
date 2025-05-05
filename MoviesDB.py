import f1director


def main():
    while True:
        display_menu()
        choice = input("Choice:")

        if (choice == 'x'):
            break
        elif (choice =="1"):
            View_Directors_and_Films()
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
    name = input("Enter name or part of name to search: ")
    directors_and_films = f1director.view_director(name)
    print("\nDirector | Film | Studio")
    print("---------------------------")
    for director in directors_and_films:
        print(f"{director['directorName']}, |, {film['FilmName']}, |, {studio['StudioName']}")


if __name__ == "__main__":
    main()