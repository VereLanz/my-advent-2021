from typing import List

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 10


CORRUPTION_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

COMPLETION_SCORE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

CLOSER_TO_OPEN_PAIRING = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def score_corrupt_syntax_lines(inputs: List[str]) -> int:
    score = 0
    for line in inputs:
        score += check_line_corruption(line)
    return score


def check_line_corruption(line: str) -> int:
    symbols = []
    for symbol in line:
        if symbol not in CLOSER_TO_OPEN_PAIRING.values():
            symbols.append(symbol)
        elif CLOSER_TO_OPEN_PAIRING[symbols.pop()] != symbol:
            return CORRUPTION_SCORES[symbol]
    return 0


def solve_a(puzzle: MyPuzzle):
    answer_a = score_corrupt_syntax_lines(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def score_complete_syntax_error_lines(inputs: List[str]) -> int:
    scores = []
    for line in inputs:
        line_score = 0
        completion = calculate_line_completion_score(line)
        for symbol in completion:
            line_score *= 5
            line_score += COMPLETION_SCORE[symbol]
        if line_score > 0:
            scores.append(line_score)
    return sorted(scores)[len(scores) // 2]


def calculate_line_completion_score(line: str) -> List[str]:
    symbols = []
    for symbol in line:
        if symbol not in CLOSER_TO_OPEN_PAIRING.values():
            symbols.append(symbol)
        elif CLOSER_TO_OPEN_PAIRING[symbols[-1]] == symbol:
            symbols.pop()
        else:  # corrupt line
            return []

    closing_symbols = []
    for symbol in symbols[::-1]:
        closing_symbols.append(CLOSER_TO_OPEN_PAIRING[symbol])
    return closing_symbols


def solve_b(puzzle: MyPuzzle):
    answer_b = score_complete_syntax_error_lines(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
