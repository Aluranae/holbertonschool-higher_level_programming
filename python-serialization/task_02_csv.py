#!/usr/bin/env python3
"""Module to convert CSV data into JSON format."""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV file to JSON format and save it to 'data.json'.
    Args:
        filename (str): Path to the input CSV file.
    Returns:
        bool: True if conversion succeeded, False otherwise.
    """
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            list_dict = list(reader)
        with open("data.json", "w") as data:
            json.dump(list_dict, data, indent=4)
        return True
    except (FileNotFoundError, PermissionError, OSError, csv.Error):
        return False
