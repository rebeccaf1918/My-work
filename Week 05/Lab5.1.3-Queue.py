# Queue.py
# Program that puts 10 random numbers into a queue(list), 
# then output all the values in the queue, 
# takes the numbers from the queue one at a time, 
# prints it and the current numbers still in the queue. 
# Author: Rebcca Feeley

import random 

queue = []

number_of_numbers = 10
range_to = 100

for n in range(0, number_of_numbers):
    queue.append(random.randint(0, range_to))

print ("queue is {}".format(queue))

while len(queue) != 0:
    current_number = queue.pop(0)
    print ("Current number is {} and the queue is {}".format(current_number, queue))


print("The queue is now empty.")