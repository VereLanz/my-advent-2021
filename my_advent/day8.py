from typing import List

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 8


def count_unique_number_digits(inputs: List[str]) -> int:
    # very basic because speed...
    notes = []
    for line in inputs:
        signal_patterns, output = line.split("|")
        signal_patterns = signal_patterns.strip().split()
        output = output.strip().split()
        notes.append((signal_patterns, output))

    counter = 0
    for _, output in notes:
        un_digits = [o for o in output if len(o) <= 4 or len(o) == 7]
        counter += len(un_digits)
    return counter


def solve_a(puzzle: MyPuzzle):
    answer_a = count_unique_number_digits(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def determine_output_digits(inputs: List[str]) -> int:
    pass


def solve_b(puzzle: MyPuzzle):
    answer_b = determine_output_digits(puzzle.input_lines)
    # puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    solve_b(my_puzzle)
