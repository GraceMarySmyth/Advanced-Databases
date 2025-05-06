import f1director
import f2actor
import f3addActor
import f6Studio

def main():
    while True:
        display_menu()
        choice = input("Choice: ")

        if choice == 'x':
            break
        elif choice =="1":
            View_Directors_and_Films()
        elif choice =="2":
            View_Actors_by_Month_of_Birth()
        elif choice == "3":
            add_Actor()
        elif choice == "6":
            studio()
        else:
            print("Invalid choice. Please try again.") 

            
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

    if not directors_and_films:
        print("--------------------------------")
        print("No directors found of that name.")    
    
    if directors_and_films:
        print("\nDirector | Film | Studio")
        print("---------------------------")
    for director in directors_and_films:
        print(f"{director['DirectorName']}, |, {director['FilmName']}, |, {director['StudioName']}")
    
   
            
def View_Actors_by_Month_of_Birth():
    month_input = input("Enter month (first 3 letters, e.g., Jan, Feb, or month number, e.g., 1, 2): ").strip()
    
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
            print(f"{actor['ActorName']} | {actor['ActorDOB']} | {actor['ActorGender']}")
    else:
        print("-------------------")
        print("No actors born in that month.")

            
            
def add_Actor():
    ActorID = input("Enter Actor ID: ")
    ActorName = input("Enter Actor Name: ")
    ActorDOB = input("Enter Actors DOB: ")
    ActorGender = input("Enter Actors Gender: ")
    ActorCountryID = input("Enter country that actor is from: ")
    
    f3addActor.add_Actor(ActorID, ActorName, ActorDOB, ActorGender, ActorCountryID)


def studio():
    studios = f6Studio.view_studio()
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
    