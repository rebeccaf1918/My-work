# writeJSON.py

# Author: Rebecca Feeley

import json

FILENAME = "testdict.json"
sample = dict(name="Rebecca", age=24, grades=[45,78,97])

def write_dict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)

# test the function
write_dict(sample)

