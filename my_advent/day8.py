from typing import List, Tuple

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 8

# "cf": "1",  # unique length (2)
# "acdeg": "2",
# "acdfg": "3",
# "bcdf": "4",  # unique length (4)
# "abdfg": "5",
# "abdefg": "6",
# "acf": "7",  # unique length (3)
# "abcdefg": "8",  # unique length (7, full)
# "abcdfg": "9",


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
    # whole method assumes there one of each digit, so no checks added
    pattern_sets = [set(p[:]) for p in patterns]
    two_three_fives = [p for p in pattern_sets if len(p) == 5]
    zero_six_nines = [p for p in pattern_sets if len(p) == 6]

    one = [p for p in pattern_sets if len(p) == 2][0]
    seven = [p for p in pattern_sets if len(p) == 3][0]
    four = [p for p in pattern_sets if len(p) == 4][0]

    two = [p for p in two_three_fives if len(p - four - seven) == 2][0]
    three = [p for p in two_three_fives if len(p - two) == 1][0]
    five = [p for p in two_three_fives if len(p - two) == 2][0]

    nine = [p for p in zero_six_nines if len(p - four - seven) == 1][0]
    six = [p for p in zero_six_nines if len(p - one) == len(p) - 1][0]
    zero = [p for p in zero_six_nines if p != nine and p != six][0]

    pattern_map = {
        "".join(sorted(zero)): "0",
        "".join(sorted(one)): "1",
        "".join(sorted(two)): "2",
        "".join(sorted(three)): "3",
        "".join(sorted(four)): "4",
        "".join(sorted(five)): "5",
        "".join(sorted(six)): "6",
        "".join(sorted(seven)): "7",
        "abcdefg": "8",
        "".join(sorted(nine)): "9",
    }

    parsed_output = [pattern_map["".join(sorted(d))] for d in output]
    return "".join(parsed_output)


def solve_b(puzzle: MyPuzzle):
    answer_b = determine_output_digits(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
