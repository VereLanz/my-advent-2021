import pytest

from my_advent.day12 import count_paths_through_system, count_more_paths_through_system

EXAMPLE_INPUT_ONE = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end",
]

EXAMPLE_INPUT_TWO = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc",
]

EXAMPLE_INPUT_THREE = [
    "fs-end",
    "he-DX",
    "fs-he",
    "start-DX",
    "pj-DX",
    "end-zg",
    "zg-sl",
    "zg-pj",
    "pj-he",
    "RW-he",
    "fs-DX",
    "pj-RW",
    "zg-RW",
    "start-pj",
    "he-WI",
    "zg-he",
    "pj-fs",
    "start-RW",
]


@pytest.mark.parametrize(
    ("connections", "paths"),
    [
        (EXAMPLE_INPUT_ONE, 10),
        (EXAMPLE_INPUT_TWO, 19),
        (EXAMPLE_INPUT_THREE, 226),
    ]
)
def test_example_a(connections, paths):
    assert count_paths_through_system(connections) == paths


def test_example_b():
    example_result = 36
    assert count_more_paths_through_system(EXAMPLE_INPUT_ONE) == example_result
