#!/usr/bin/python3

# This function prints the numbers from 1 to 100.
# For multiples of 3, it prints "Fizz" instead of the number.
# For multiples of 5, it prints "Buzz".
# For multiples of both 3 and 5, it prints "FizzBuzz".
# Each output is followed by a space.


def fizzbuzz():

    for i in range(1, 101):

        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")

        elif i % 3 == 0:
            print("Fizz", end=" ")

        elif i % 5 == 0:
            print("Buzz", end=" ")

        else:
            print(i, end=" ")
