from my_advent.day13 import fold_and_count_dots, fold_and_show_dots

EXAMPLE_INPUT = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5",
]


def test_example_a():
    example_result = 17
    assert fold_and_count_dots(EXAMPLE_INPUT) == example_result


def test_example_b():
    # should print a matrix with 1s shaped like a square (+ 2 zero rows)
    fold_and_show_dots(EXAMPLE_INPUT)
