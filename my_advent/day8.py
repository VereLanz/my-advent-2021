from typing import List, Tuple

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 8

SEGMENTS_TO_DIGIT = {
    "cf": "1",  # unique length (2)
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",  # unique length (4)
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",  # unique length (3)
    "abcdefg": "8",  # unique length (7, full)
    "abcdfg": "9",
}


def count_unique_number_digits(inputs: List[str]) -> int:
    # very basic because speed...
    notes = parse_notes(inputs)
    counter = 0
    for _, output in notes:
        un_digits = [o for o in output if len(o) <= 4 or len(o) == 7]
        counter += len(un_digits)
    return counter


def parse_notes(inputs: List[str]) -> List[Tuple[List[str], List[str]]]:
    notes = []
    for line in inputs:
        signal_patterns, output = line.split("|")
        signal_patterns = signal_patterns.strip().split()
        output = output.strip().split()
        notes.append((signal_patterns, output))
    return notes


def solve_a(puzzle: MyPuzzle):
    answer_a = count_unique_number_digits(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def determine_output_digits(inputs: List[str]) -> int:
    notes = parse_notes(inputs)
    output_numbers = []
    for patterns, output in notes:
        parsed_output = translate_output_pattern(patterns, output)
        output_numbers.append(int(parsed_output))
    return sum(output_numbers)


def translate_output_pattern(patterns: List[str], output: List[str]) -> str:
    # determine what we know from patterns (+ output?)
    # find a translation (matrix?) for this pattern
    # translate output
    translated_output = []

    parsed_output = [SEGMENTS_TO_DIGIT["".join(sorted(d))] for d in translated_output]
    return "".join(parsed_output)


def solve_b(puzzle: MyPuzzle):
    answer_b = determine_output_digits(puzzle.input_lines)
    # puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    solve_b(my_puzzle)
