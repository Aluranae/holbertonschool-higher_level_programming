#!/usr/bin/python3

"""Module defining a CountedIterator that tracks iteration count."""


class CountedIterator:
    """Custom iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable and start counter at 0."""
        self.__iterable = iter(iterable)
        self.__count = 0

    def get_count(self):
        """Return the number of items that have been iterated."""
        return self.__count

    def __next__(self):
        """Return next item and increment counter.\
            Raise StopIteration if done."""
        item = next(self.__iterable)
        self.__count += 1
        return item

    def __iter__(self):
        """Return self to allow iteration with for-loop."""
        return self
