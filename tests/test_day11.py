import pytest

from my_advent.day11 import count_flashing_octopi, find_flashy_step

EXAMPLE_INPUT = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]


@pytest.mark.parametrize(
    "steps, result",
    [
        (10, 204),
        (100, 1656),
    ]
)
def test_example_a(steps, result):
    assert count_flashing_octopi(EXAMPLE_INPUT, steps=steps) == result


def test_example_b():
    example_result = 195
    assert find_flashy_step(EXAMPLE_INPUT) == example_result
