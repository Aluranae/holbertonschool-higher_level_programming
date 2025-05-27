#!/usr/bin/python3

"""Module defining Fish, Bird, and FlyingFish\
    classes using multiple inheritance."""


class Fish:
    """A fish that can swim and lives in water."""

    def swim(self):
        """Print swimming behavior of fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat of fish."""
        print("The fish lives in water")


class Bird:
    """A bird that can fly and lives in the sky."""

    def fly(self):
        """Print flying behavior of bird."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat of bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A flying fish that inherits from Fish and Bird."""

    def fly(self):
        """Override flying behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swimming behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat to show dual nature."""
        print("The flying fish lives both in water and the sky!")
