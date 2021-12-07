from typing import List

import numpy as np

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 7


def find_minimum_fuel_alignment(inputs: List[str]) -> int:
    positions = [int(i) for i in inputs[0].split(",")]
    cheapest_position = int(np.median(positions))
    fuel_needed = sum([abs(cheapest_position - p) for p in positions])
    return fuel_needed


def find_minimum_non_linear_fuel_alignment(inputs: List[str]) -> int:
    positions = [int(i) for i in inputs[0].split(",")]
    # rounding method leads to different positions, we need to check both
    cheapest_pos_f = np.floor(np.mean(positions))
    fuel_needed_f = sum([sum_factorial(abs(cheapest_pos_f - p)) for p in positions])
    cheapest_pos_c = np.ceil(np.mean(positions))
    fuel_needed_c = sum([sum_factorial(abs(cheapest_pos_c - p)) for p in positions])
    return min(fuel_needed_f, fuel_needed_c)


def sum_factorial(start: int, end: int = 1) -> int:
    arithmetic_factorial_sum = (start + end) * start / 2  # should always be an even int
    return int(arithmetic_factorial_sum)


def solve_a(puzzle: MyPuzzle):
    answer_a = find_minimum_fuel_alignment(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = find_minimum_non_linear_fuel_alignment(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
