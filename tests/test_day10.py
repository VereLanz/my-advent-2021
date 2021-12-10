from my_advent.day10 import score_corrupt_syntax_lines, score_complete_syntax_error_lines

EXAMPLE_INPUT = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


def test_example_a():
    example_result = 26397
    assert score_corrupt_syntax_lines(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 288957
    assert score_complete_syntax_error_lines(EXAMPLE_INPUT) == example_result
