# Studentextra.py
# user can input their data for data structure
# (not 100% this fulfils the lab brief but the code works)
# Author: Rebecca Feeley

student = (input("Enter your student name here: "))  


module_dict = {}
modules = int(input("Enter the number of modules you study: "))

for i in range (modules):
    key = input ("Enter course name: ")
    value = input ("Enter grade: ")
    module_dict.update({key: value})
print (student, module_dict)


    
