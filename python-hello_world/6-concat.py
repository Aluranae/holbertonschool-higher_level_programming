#!/usr/bin/python3

# This script creates a welcome message
# using two string variables and an f-string

str1 = "Holberton"
str2 = "School"
str1 += " {}".format(str2)
print(f"Welcome to {str1}!")
