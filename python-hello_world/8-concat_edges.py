#!/usr/bin/python3

# This script rebuilds a specific sentence using slicing and concatenation,
# without new variables

str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"

str = str[39:66] + str[106:112] + str[:6]

print(str)
