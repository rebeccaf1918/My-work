# isEven.py
# Program prompts the reader for number
# and indicates if the number is even or odd 

# Author: Rebecca Feeley

number = int(input("enter an integer: "))

if (number % 2) == 0:
    print (f"{number} is an even number.")

else:
    print (f"{number} is an odd number.")

