#!/usr/bin/env python3
"""Module for serializing and deserializing a custom
Python object using pickle."""

import pickle


class CustomObject:
    """
    Custom class with attributes and pickle-based serialization methods.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Is Student: ", self.is_student)

    def serialize(self, filename):
        """
        Serialize the object and save it to the specified file using pickle.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (FileNotFoundError, pickle.PicklingError, PermissionError,
                OSError):
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        Load an object from the specified file using pickle.
        Returns:
            CustomObject instance or None if error occurs.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, PermissionError, pickle.UnpicklingError,
                EOFError, OSError, AttributeError):
            return None
