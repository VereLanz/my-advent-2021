from my_advent.day14 import score_full_chain

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
    assert score_full_chain(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 2_188_189_693_529
    assert score_full_chain(EXAMPLE_INPUT, steps=40) == example_result
