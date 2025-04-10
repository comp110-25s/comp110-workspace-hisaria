"""Practicing with dictionary functions!"""

__author__ = "730748060"


def invert(changes: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary's keys and values."""

    inverted = {}
    keys = list(changes.keys())  # Find a list of keys from the original dictionary

    i = 0
    while i < len(keys):
        key = keys[i]
        value = changes[key]
        if value in inverted:
            raise KeyError("Duplicate value found: " + value)
        else:
            inverted[value] = key
        i += 1

    return inverted


def count(counts: list[str]) -> dict[str, int]:
    """Holds count for how many times the number appears."""

    count_dict = {}  # Initialize an empty dictionary to store counts
    i = 0
    while i < len(counts):
        item = counts[i]
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
        i += 1
    return count_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Finds and retuns the most commonly found color in the dictionary."""

    color_count = {}  # Empty dictionary to store color counts
    names = list(colors.keys())
    i = 0

    # Counts the frequency of every single color
    while i < len(names):
        color = colors[names[i]]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        i += 1

    # Finds the color that appears most frequently
    most_frequent_color = None
    max_count = 0

    i = 0
    while i < len(names):
        color = colors[names[i]]
        if color_count[color] > max_count:
            most_frequent_color = color
            max_count = color_count[color]
        i += 1

    return most_frequent_color


def bin_len(bins: list[str]) -> dict[int, set[str]]:
    """Bins a list of strings into a dictionary."""
    bin_dict = {}
    i = 0

    while i < len(bins):
        string = bins[i]
        length = len(string)

        if length not in bin_dict:
            bin_dict[length] = set()

        bin_dict[length].add(string)
        i += 1

    return bin_dict
