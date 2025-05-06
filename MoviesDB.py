import f1director
import f2actor
import f3addActor
import f6studio

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
    if directors_and_films:
        print("\nDirector | Film | Studio")
        print("---------------------------")
    for director in directors_and_films:
        print(f"{director['directorName']}, |, {film['FilmName']}, |, {studio['StudioName']}")
    if not directors_and_films:
            print("-----------------------------")  
            print("No directors found of that name.")
            return    

def View_Actors_by_Month_of_Birth():
    month_input = input("Enter month (first 3 letters, e.g., Jan, Feb, or month number, e.g., 1, 2): ").strip()
    
    # Normalize input to month abbreviation
    if month_input.isdigit():
        month_number = int(month_input)
        if 1 <= month_number <= 12:
            month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][month_number - 1]
        else:
            print("Invalid month number. Please try again.")
            return
    else:
        month = month_input.capitalize()
    
    actors_by_month = f2actor.view_actor(month)
    if actors_by_month:
        print("\nActor | DOB | Gender")
        print("------------------------")
        for actor in actors_by_month:
            print(f"{actor['ActorName']}, |, {actor['ActorDOB']}, |, {actor['ActorGender']}")
    else:
        print("-------------------")
        print("No actors born in that month.")
        return
    

def add_Actor():
    ActorID = input("Enter Actor ID: ")
    ActorName = input("Enter Actor Name: ")
    ActorDOB = input("Enter Actors DOB: ")
    ActorCountryID = input("Enter country that actor is from: ")
    
    f3addActor.add_Actor(ActorID, ActorName, ActorDOB, ActorCountryID)
    print("Actor successfully added. Returning to the main menu.")
    return

def studio():
    studios = f6studio.view_studios()
    if studios:
        print("\nStudio ID | Studio Name")
        print("------------------------")
        for studio in sorted(studios, key=lambda x: x['StudioID']):
            print(f"{studio['StudioID']} | {studio['StudioName']}")
    else:
        print("-------------------")
        print("No studios found.")
  

if __name__ == "__main__":
    main()