# sub.py
# Program to subtract one number from another
# input reads in a string so I need to convert it into an int
# in order to perform mathematical operations

# Authoer: Rebecca Feeley

x = int(input("Enter first number: ")) 
y = int(input("Enter second number: "))

answer = x - y

print ("{} minus {} is {} ".format(x, y, answer))
