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
    print("Directors and Films")






if __name__ == "__main__":
    main()