import pytest

from my_advent.day5 import find_overlapping_vents

EXAMPLE_INPUT = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]


def test_example_a():
    example_result = 5
    assert find_overlapping_vents(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 12
    # now with diagonals also considered
    assert find_overlapping_vents(EXAMPLE_INPUT, diagonals=True) == example_result
