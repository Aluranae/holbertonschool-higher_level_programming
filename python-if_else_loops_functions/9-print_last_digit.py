#!/usr/bin/python3

# This function prints the last digit of a number and returns it.
# If the number is negative, it returns the positive value of the last digit.

def print_last_digit(number):

    last_dig = abs(number) % 10
    print(last_dig, end="")
    return last_dig
