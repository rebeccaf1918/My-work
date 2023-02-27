message = 'I have eaten ' + 99 + ' burritos.'
print (message)

# The above program will not work, giving error message "can only concatenate str(not 'int') to str"

message = "I have eaten " + str(99) + " burritos. " # alter integer to string to program can concatenate str to str

print (message)