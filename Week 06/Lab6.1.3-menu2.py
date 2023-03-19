# menu2.py
# Program that keeps displaying the menu until the user chooses q
# Author: Rebecca Feeley

def display_menu():
    print ("What would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View students")
    print ("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice 

def do_add():
    # to be filled in later
    print ("in adding")

def do_view():
    # to be filled in later
    print ("in viewing")

choice = display_menu()
while (choice != "q"): 
    if choice == "a":
        do_add()
    elif choice == "v":
        do_view()
    elif choice != "q":
        print("\n\nplease select either a,v or q")
    choice = display_menu()

