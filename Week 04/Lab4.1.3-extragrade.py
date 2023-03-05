import math

percentage = float(input("Enter a percentage: "))

percentage = (math.ceil(percentage)) # this rounds up any percentage with a decimal e.g 69.5 to 70

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