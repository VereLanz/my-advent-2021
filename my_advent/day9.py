from typing import List

import numpy as np
from scipy.ndimage import minimum_filter

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 9


def find_area_risk_score(inputs: List[str]) -> int:
    map_x = len(inputs[0])
    map_y = len(inputs)
    height_map = np.fromstring(",".join("".join(inputs)[:]), dtype=int, sep=",").reshape((map_y, map_x))
    local_minima_mask = minimum_filter(height_map, size=3, mode="constant", cval=9)
    local_minima = height_map[height_map == local_minima_mask]
    risk_score = np.sum(local_minima) + len(local_minima)
    return risk_score


def solve_a(puzzle: MyPuzzle):
    answer_a = find_area_risk_score(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = (puzzle.input_lines)
    # puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    solve_a(my_puzzle)
    # solve_b(my_puzzle)
