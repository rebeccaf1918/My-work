# readdict.py

# Author: Rebecca Feeley

import json

FILENAME = "testdict.json"
def read_dict():
    # this will be an error if file doesnt exist 
    # later lectures will how why it should just return an empty dict 
    with open(FILENAME) as f:
        return json.load(f)

# test the function
some_dict = read_dict()
print (some_dict)


