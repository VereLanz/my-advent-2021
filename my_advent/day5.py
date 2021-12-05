from typing import List, Tuple

import numpy as np

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 5


def find_overlapping_vents(inputs: List[str], diagonals: bool = False) -> int:
    vent_lines = get_vent_coordinates(inputs)
    vent_coords = get_all_vent_coordinates(vent_lines, diagonals=diagonals)

    grid_size_x = max([max(line[0][0], line[1][0]) for line in vent_lines]) + 1
    grid_size_y = max([max(line[0][1], line[1][1]) for line in vent_lines]) + 1
    grid = np.zeros(shape=(grid_size_y, grid_size_x))
    for x, y in vent_coords:
        # (x, y) -> array[y][x]
        grid[y][x] += 1

    overlap_count = len(grid[grid >= 2])
    return overlap_count


def get_vent_coordinates(inputs: List[str]) -> List[List[Tuple[int, int]]]:
    vent_lines = []
    for line in inputs:
        vent_start, vent_end = [point.split(",") for point in line.split(" -> ")]
        vent_start = (int(vent_start[0]), int(vent_start[1]))
        vent_end = (int(vent_end[0]), int(vent_end[1]))
        vent_lines.append([vent_start, vent_end])
    return vent_lines


def get_all_vent_coordinates(vent_lines: List[List[Tuple[int, int]]], diagonals: bool = False) -> List[Tuple[int, int]]:
    vent_coords = []
    # find all points of a line to the line's coordinates
    for vent_line in vent_lines:
        start_x, start_y = vent_line[0]
        end_x, end_y = vent_line[1]
        # vertical line
        if start_x == end_x:
            y = min(start_y, end_y)
            while y <= max(start_y, end_y):  # add start and end point as well
                vent_coords.append((start_x, y))
                y += 1
        # horizontal line
        elif start_y == end_y:
            x = min(start_x, end_x)
            while x <= max(start_x, end_x):  # add start and end point as well
                vent_coords.append((x, start_y))
                x += 1
        # diagonal lines
        else:
            if not diagonals:  # skip for part one
                continue
            x = start_x
            y = start_y
            goal = (end_x, end_y)
            x_mod = np.sign(end_x - start_x)
            y_mod = np.sign(end_y - start_y)
            while (x, y) != goal:
                vent_coords.append((x, y))
                x += x_mod
                y += y_mod
            # add the end point explicitly
            vent_coords.append((x, y))

    return vent_coords


def solve_a(puzzle: MyPuzzle):
    answer_a = find_overlapping_vents(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    # now with diagonals
    answer_b = find_overlapping_vents(puzzle.input_lines, diagonals=True)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
