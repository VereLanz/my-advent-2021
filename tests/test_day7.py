from my_advent.day7 import (
    find_minimum_fuel_alignment,
    find_minimum_non_linear_fuel_alignment,
)

EXAMPLE_INPUT = [
    "16,1,2,0,4,2,7,1,2,14",
]


def test_example_a():
    example_result = 37
    assert find_minimum_fuel_alignment(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 168
    assert find_minimum_non_linear_fuel_alignment(EXAMPLE_INPUT) == example_result
