from my_advent.day15 import find_lowest_risk_path

EXAMPLE_INPUT = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581",
]


def test_example_a():
    example_result = 40
    assert find_lowest_risk_path(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 0
    assert (EXAMPLE_INPUT) == example_result
