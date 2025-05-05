#!/usr/bin/python3

# This program prints all different combinations of two digits,
# without repetition and in ascending order,
# using at most two loops and three print functions.


for i in range(10):
    for j in range(i + 1, 10):
        if i != 8 or j != 9:
            print(f"{i}{j}, ", end="")
        else:
            print(f"{i}{j}")
