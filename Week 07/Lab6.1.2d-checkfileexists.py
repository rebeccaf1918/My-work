# checkfileexists.py

# Author: Rebecca Feeley

def write_number(number):
    with open (FILENAME, "wt") as f:
        # write takes in a string so it must be be converted
        f.write(str(number))

import os.path

FILENAME = "count2.txt"
if not os.path.isfile(FILENAME):
    print ("File does not exist")
    write_number(0)

