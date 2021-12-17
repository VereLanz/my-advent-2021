from my_advent.day17 import shoot_high

EXAMPLE_INPUT = [
    "target area: x=20..30, y=-10..-5",
]


def test_example_a():
    example_result = 45  # starting velocity 6,9
    assert shoot_high(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 0
    assert (EXAMPLE_INPUT) == example_result
