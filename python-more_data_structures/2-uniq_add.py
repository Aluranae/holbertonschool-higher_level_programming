#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    uniq = set(my_list)
    for element in uniq:
        sum += element
    return sum
