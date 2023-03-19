# together1.py
# the array in which the whole lab task is put together
# Author: Rebecca Feeley

def display_menu():
    print ("What would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View students")
    print ("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice 

students = []

def do_add(students):
    current_student = {}
    current_student["name"]=input("Enter name: ")
    current_student["modules"]= read_modules()
    students.append(current_student)

def read_modules():
    modules = []
    module_name = input("\tEnter the first Module name (blank to quit): ").strip()

    while module_name != "":
        module = {}
        module["name"] = module_name
        module["grade"]=int(input("\t\tEnter grade: "))
        modules.append(module)
        # now to read in the next module name
        module_name = input("\tEnter next module name (blank to quit): ").strip()
    
    return modules 

def do_view(students):
    # to be filled in later as per doView.py file 
    print ("in viewing")

students = []

choice = display_menu()
while (choice != "q"): 
    if choice == "a":
        do_add(students)
    elif choice == "v":
        do_view(students)
    elif choice != "q":
        print("\n\nplease select either a,v or q")
    choice = display_menu()
