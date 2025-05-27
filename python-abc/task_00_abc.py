#!/usr/bin/python3

"""Module defining an abstract Animal class and its concrete subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing a generic animal."""
    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class implementing the sound method."""
    def sound(self):
        """Return the sound made by the dog."""
        return ("Bark")


class Cat(Animal):
    """Cat class implementing the sound method."""
    def sound(self):
        """Return the sound made by the cat."""
        return ("Meow")
