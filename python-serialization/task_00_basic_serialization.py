#!/usr/bin/env python3
"""Module that provides JSON serialization and deserialization functions."""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a dictionary and save it to a JSON file.
    If the file already exists, it will be replaced.
    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Name of the file to save the JSON data.
    """
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and return it as a Python dictionary.
    Args:
        filename (str): Name of the file to load the JSON data from.
    Returns:
        dict: The dictionary deserialized from the JSON file.
    """

    with open(filename, "r") as file:
        return json.load(file)
