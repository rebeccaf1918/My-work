# absolute.py
# Gives the absolute value of number

# Author: Rebecca Feeley

# In the question, the number is ambiguous bu thte output imples that we should be using floats
# So, I am casting the input to a float
number = float(input("Enter a number: "))
absolute_value = abs(number)

print ("The absolute value of {} is {}".format(number,absolute_value))


