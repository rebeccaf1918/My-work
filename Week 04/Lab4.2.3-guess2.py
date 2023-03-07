# guess2.py
# prompts the user to guess a number and stops when they get it right
# the program will tell the user if they were too high or too low
# Author: Rebecca Feeley

numberToGuess = 30

guess = int(input("Please enter the number: "))

while guess != numberToGuess:
    print ("Wrong")
    if guess < numberToGuess:
        print ("Too low")
    else:
        print ("Too high")
    guess = int(input("Please guess again: "))
    
# this is an alternative way of printing out variables

print ("Well done! Yes, the number was ", numberToGuess)