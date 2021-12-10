from typing import List

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 10


CORRUPTION_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

OPEN_TO_CLOSE_PAIRING = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}


def score_corrupt_syntax_lines(inputs: List[str]) -> int:
    score = 0
    for line in inputs:
        score += check_line_corruption(line)
    return score


def check_line_corruption(line: str) -> int:
    # find wrong closing symbol, something with list appending and pop/peek?
    # score the wrong closing symbols
    # return sum of scores or 0 if not corrupt
    pass


def solve_a(puzzle: MyPuzzle):
    answer_a = (puzzle.input_lines)
    # puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = (puzzle.input_lines)
    # puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    solve_a(my_puzzle)
    # solve_b(my_puzzle)
