#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")
