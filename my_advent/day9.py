from functools import reduce
from typing import List

import numpy as np
from scipy.ndimage import minimum_filter
from scipy.ndimage.measurements import label

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 9


def find_area_risk_score(inputs: List[str]) -> int:
    map_x = len(inputs[0])
    map_y = len(inputs)
    height_map = np.fromstring(
        ",".join("".join(inputs)[:]), dtype=int, sep=","
    ).reshape((map_y, map_x))
    local_minima_mask = minimum_filter(height_map, size=3, mode="constant", cval=9)
    local_minima = height_map[height_map == local_minima_mask]
    # scoring for each minima is its height + 1
    risk_score = np.sum(local_minima + 1)
    return int(risk_score)


def solve_a(puzzle: MyPuzzle):
    answer_a = find_area_risk_score(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def score_big_basins(inputs: List[str]) -> int:
    map_x = len(inputs[0])
    map_y = len(inputs)
    height_map = np.fromstring(
        ",".join("".join(inputs)[:]), dtype=int, sep=","
    ).reshape((map_y, map_x))

    # for label function, 0s are background, everything else is signal
    # we want to find connected basins that are split by 9s -> 9 is background
    height_map[height_map != 9] = 1
    height_map[height_map == 9] = 0
    # default label search structure: touching sideways counts, diagonally does not
    basin_labels, basin_count = label(height_map)
    # the labels are numbered 1 to n for every group
    basin_sizes = [len(basin_labels[basin_labels == i + 1]) for i in range(basin_count)]
    biggest_basins = sorted(basin_sizes)[-3:]
    return reduce(lambda x, y: x * y, biggest_basins)


def solve_b(puzzle: MyPuzzle):
    answer_b = score_big_basins(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
