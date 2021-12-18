from my_advent.day17 import shoot_high, find_all_shots

EXAMPLE_INPUT = [
    "target area: x=20..30, y=-10..-5",
]


def test_example_a():
    example_result = 45  # starting velocity 6,9
    assert shoot_high(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 112
    assert find_all_shots(EXAMPLE_INPUT) == example_result
