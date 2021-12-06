from my_advent.day6 import calculate_spawns, calculate_massive_spawns

EXAMPLE_INPUT = [
    "3,4,3,1,2"
]


def test_example_a():
    example_result = 5934
    assert calculate_spawns(EXAMPLE_INPUT, days=80) == example_result


def test_example_b():
    example_result = 26_984_457_539
    assert calculate_massive_spawns(EXAMPLE_INPUT, days=256) == example_result
