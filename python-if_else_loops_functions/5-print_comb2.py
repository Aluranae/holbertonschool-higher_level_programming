#!/usr/bin/python3

# This program prints numbers from 00 to 99 with leading zeros,
# separated by ', ', using only one loop and at most two print functions.

for i in range(100):
    if i < 99:
        print(f"{i:02}, ", end="")
    else:
        print(f"{i:02}")
