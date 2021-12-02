from my_advent.day2 import move_submarine_path, move_submarine_with_aim

EXAMPLE_INPUT = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def test_example_a():
    example_result = 150
    assert move_submarine_path(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 900
    assert move_submarine_with_aim(EXAMPLE_INPUT) == example_result
