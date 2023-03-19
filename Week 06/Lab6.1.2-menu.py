# menu.py
# gives the use a choice of 3 options and outputs their choice
# Author: Rebecca Feeley

def display_menu():
    print ("What would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View students")
    print ("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice 

# test the function
choice = display_menu()
print (f"you chose {choice}")

