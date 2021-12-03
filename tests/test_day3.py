from my_advent.day3 import calculate_power_consumption, calculate_life_support

EXAMPLE_INPUT = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_example_a():
    example_result = 198
    assert calculate_power_consumption(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 230
    assert calculate_life_support(EXAMPLE_INPUT) == example_result
