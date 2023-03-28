# readnumber.py
# a function that reads in a number from a file that already exists (count.txt)
# Author: Rebecca Feeley

FILENAME = "count.txt"
def read_number():
    with open(FILENAME) as f:
        number = int(f.read())
        return number

# test function works
num = read_number()
print (num)

