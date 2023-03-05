# grade.py
# This program reads in a student's percentage 
# and prints out the corresponding grade

# Author: Rebecca Feeley

percentage = float(input("Enter a percentage: "))
#print (percentage) # this is for debugging
percentage = round(percentage)

if percentage < 40: #between 0 and 39
    print ("Fail")
elif percentage < 50: #between 40 and 49
    print ("Pass")
elif percentage < 60: #between 50 and 59
    print ("Merit1")
elif percentage < 70: #between 60 and 69
    print ("Merit2")
else: # the only option left is between 70 and 100
    print ("Distinction")