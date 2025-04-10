"""Practicing with Unit Tests!"""

__author__ = "730748060"

import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

from exercises.ex03.dictionary import invert


def test_invert_edge():
    # Edge case: empty dictionary
    assert invert({}) == {}


def test_invert_case1():
    # Use case 1: tests inverting of values
    assert invert({"a": "b", "c": "d", "e": "f"}) == {"b": "a", "d": "c", "f": "e"}


def test_invert_case2():
    # Use case 2: raises KeyError for duplicates
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


from exercises.ex03.dictionary import count


def test_count_edge():
    # Edge case: empty list
    assert count([]) == {}


def test_count_case1():
    # Use case 1: testing counts of repeats
    assert count(["pillow", "pillow", "pillow"]) == {"pillow": 3}


def test_count_case2():
    # Use case 2: testing counts of different elements
    assert count(["pillow", "blanket", "bed"]) == {
        "pillow": 1,
        "blanket": 1,
        "bed": 1,
    }


from exercises.ex03.dictionary import favorite_color


def test_favorite_color_edge():
    # Edge case: empty dictionary
    assert favorite_color({}) == None


def test_favorite_color__case1():
    # Use case 1: testing even with one color
    assert favorite_color({"Nikki": "blue"}) == "blue"


def test_favorite_color__case2():
    # Use case 2: testing most common color
    assert favorite_color({"Nikki": "red", "Siya": "blue", "Amy": "blue"}) == "blue"


from exercises.ex03.dictionary import bin_len


def test_bin_len_edge():
    # Edge case: empty list
    assert bin_len([]) == {}


def test_bin_len__case1():
    # Use case 1: testing binning from word length
    assert bin_len(["the", "quick", "fox"]) == {
        3: {"the", "fox"},
        5: {"quick"},
    }


def test_bin_len__case2():
    # Use case 2: testing binning word length even with duplicates
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}
