#!/usr/bin/python3
"""
This script adds all command-line arguments to a list\
    and saves it to a JSON file.
"""

import sys
from os import path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

if __name__ == "__main__":
    if path.exists(filename):
        the_obj = load_from_json_file(filename)
    else:
        the_obj = []
    the_obj.extend(sys.argv[1:])
    save_to_json_file(the_obj, filename)
