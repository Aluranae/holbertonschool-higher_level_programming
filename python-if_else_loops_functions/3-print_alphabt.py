#!/usr/bin/python3

# This program prints the lowercase ASCII alphabet except 'e' and 'q',
# using one loop and one print function, without variables or imports.

for i in range(97, 123):
    if i == ord('e') or i == ord('q'):
        continue
    print(chr(i), end="")
