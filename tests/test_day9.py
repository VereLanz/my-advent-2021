from my_advent.day9 import find_area_risk_score, score_big_basins

EXAMPLE_INPUT = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]


def test_example_a():
    example_result = 15
    assert find_area_risk_score(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 1134
    assert score_big_basins(EXAMPLE_INPUT) == example_result
