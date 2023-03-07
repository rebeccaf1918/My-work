#guessextra.py

# Author: Rebecca Feeley
import random

numberToGuess = random.randint(0,100)

guess = int(input("Please enter the number: "))

while guess != numberToGuess:
    if guess < numberToGuess:
        print ("Too low")
    else:
        print ("Too high")
    guess = int(input("Please guess again: "))
    
# this is an alternative way of printing out variables

print ("Well done! Yes, the number was ", numberToGuess)