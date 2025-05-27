#!/usr/bin/python3

"""Module defining VerboseList, a custom list subclass that prints\
    notifications on changes."""


class VerboseList(list):
    """Custom list class that prints messages when modified."""

    def append(self, item):
        """Append item to list and print a message."""
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, iterable):
        """Extend list and print the number of items added."""
        super().extend(iterable)
        nb = len(iterable)
        print("Extended the list with {} items.".format(nb))

    def remove(self, item):
        """Remove item from list and print a message."""
        print("Removed {} from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item from list at given index and print a message."""
        element = super().pop(index)
        print("Popped {} from the list.".format(element))
        return element
