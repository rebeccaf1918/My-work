# count.py
# program that counts how many times the program has been run
# (uses two previous functions created)
# Author: Rebecca Feeley

FILENAME = "count.txt"

def read_number():
    with open(FILENAME) as f:
        number = int(f.read())
        return number

def write_number(number):
    with open (FILENAME, "wt") as f:
        # write takes in a string so it must be be converted
        f.write(str(number))

num = read_number()
num += 1
print ("we have run this program {} times".format(num))
write_number(num)