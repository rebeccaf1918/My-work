# isEven2.py
# Program prompts the reader for number and indicates if the number is even or odd 
# Also, keeps prompting the user for a number until the user enters -1
# Author: Rebecca Feeley

number = int(input("Enter an integer (-1 to quit): "))

while number != -1:
    if (number % 2) == 0:
        print (f"{number} is an even number.")
    else:
        print (f"{number} is an odd number.")
    number = int(input("Please enter another integer: "))

print ("This loop now finished.")





