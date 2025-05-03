def main():
    while True:
        display_menu()
        choice = input("Choice:")
    
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

if __name__ == "__main__":
    main()