import pytest

from my_advent.day14 import score_full_chain, score_full_chain_efficiently

EXAMPLE_INPUT = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C",
]


def test_example_a():
    example_result = 1588
    assert score_full_chain(EXAMPLE_INPUT, steps=10) == example_result


@pytest.mark.parametrize(
    ("steps", "score"),
    [
        (1, 2 - 1),
        (2, 6 - 1),
        (3, 11 - 4),
        (4, 23 - 5),
    ]
)
def test_smaller_example(steps, score):
    assert score_full_chain_efficiently(EXAMPLE_INPUT, steps=steps) == score


def test_example_b():
    example_result = 2_188_189_693_529
    assert score_full_chain_efficiently(EXAMPLE_INPUT, steps=40) == example_result
