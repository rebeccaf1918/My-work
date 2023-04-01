# writenumber.py
# This is a function that takes in a number and overwrites a file with that number
# Author: Rebecca Feeley


FILENAME = "count.txt"
def write_number(number):
    with open (FILENAME, "wt") as f:
        # write takes in a string so it must be be converted
        f.write(str(number))

# test the function works
write_number (0)

