#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.items():
        result = value*2
        new_dict[key] = result
    return new_dict
