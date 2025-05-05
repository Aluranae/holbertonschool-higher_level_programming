#!/usr/bin/python3

# This program checks if a randomly generated number is positive,
# zero or negative
# and prints the number followed by the corresponding message.


import random
number = random.randint(-10, 10)

if number > 0:
    print(f"{number} is positive")

elif number == 0:
    print(f"{number} is zero")

else:
    print(f"{number} is negative")
