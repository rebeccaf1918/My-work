# round.py
# Rounds a number
# Should note that it only rounds to the nearest even number
# e.g 4.5 rounds to 4 BUT 5.5 rounds to 6
# so, it should not be used where accuracy is essential

# Author: Rebecca Feeley

number_to_round = float(input("enter a float number: "))
rounded_number = round(number_to_round)
print ("{} rounded is {}".format(number_to_round,rounded_number))

