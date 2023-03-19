# readModules.py
# Program to read in the modules and student names and grades
# Author: Rebecca Feeley

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

def do_add(students):
    current_student = {}
    current_student["name"]=input("Enter name: ")
    current_student["modules"]= read_modules()

    students.append(current_student)

# test
students = []
do_add(students)

do_add(students)
print (students)