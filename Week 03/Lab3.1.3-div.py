# div.py
# This is a prgram that reads in two numbers and
# outputs the integer answer and remainder

# Author: Rebecca Feeley

x = int(input("Enter first number "))

y = int(input("Enter second number "))

answer = int(x//y) # // gives the integer division
remainder = x%y # % gives the remainder

print ("{} divided by {} is {} with remainder {}".format( x, y, answer, remainder))




