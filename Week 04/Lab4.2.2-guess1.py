# guess1.py
# prompts the user to guess a number,
# keeps prompting the user to guess the number until they get the right one

# Author: Rebecca Feeley

numberToGuess = 30

guess = int(input("Please enter the number: "))

while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again: "))
# this is an alternative way of printing out variables

print ("Well done! Yes, the number was ", numberToGuess)


