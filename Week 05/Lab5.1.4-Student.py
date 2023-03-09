# Student.py
# Program that stores a student name and a list of courses and grades in a dict, 
# Program should then print out data.
# The number of courses could change.
# Author: Rebecca Feeley

student = {
    "name" : "Mary",
    "modules" : [
        {
            "course_name" : "Programming",
            "grade" : 45
        },
        { 
            "course_name" : "History",
            "grade" : 99,
        }
    ]
}
    
        

print("Student: {}".format(student["name"]))

# modules in an array in the dict student
for module in student["modules"]:
    print("\t {} \t: {}".format(module["course_name"], module["grade"]))

