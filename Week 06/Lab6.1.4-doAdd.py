# doAdd.py
# program to add in the students' names
# Author: Rebecca Feeley

students = []

def read_modules():
    return []

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


