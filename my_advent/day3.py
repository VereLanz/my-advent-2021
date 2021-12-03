from collections import Counter
from typing import List

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 3


def calculate_power_consumption(inputs: List[str]) -> int:
    gamma = ""
    epsilon = ""
    # it's safe to assume every element has the same length
    for i in range(len(inputs[0])):
        position_bits = "".join([bits[i] for bits in inputs])
        bit_commons = Counter(position_bits).most_common(2)
        gamma += bit_commons[0][0]
        epsilon += bit_commons[1][0]
    return int(gamma, 2) * int(epsilon, 2)


def solve_a(puzzle: MyPuzzle):
    answer_a = calculate_power_consumption(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def calculate_life_support(inputs: List[str]) -> int:
    o2_gen = ""
    co2_scrub = ""

    return int(o2_gen, 2) * int(co2_scrub, 2)


def solve_b(puzzle: MyPuzzle):
    answer_b = (puzzle.input_lines)
    # puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    solve_a(my_puzzle)
    # solve_b(my_puzzle)
