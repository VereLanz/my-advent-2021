from typing import List, Tuple

import numpy as np
from scipy.signal import convolve2d

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 11


FLASH_MASK = np.ones((3, 3))


def count_flashing_octopi(inputs: List[str], steps: int = 100) -> int:
    octo_x = len(inputs[0])
    octo_y = len(inputs)
    grid_vals = ",".join("".join(inputs)[:])
    octopi = np.fromstring(grid_vals, dtype=float, sep=",").reshape((octo_y, octo_x))

    flash_count = 0
    for _ in range(steps):
        # assume at step 0 there is no >9 yet
        octopi += 1
        octopi, flashes = determine_flashes(octopi)
        flash_count += flashes
    return flash_count


def determine_flashes(octopi: np.ndarray) -> Tuple[np.ndarray, int]:
    flash_count = 0
    run = True
    while run:
        run = False
        flashers = np.ma.masked_where(octopi > 9, octopi).mask.astype(int)
        if np.sum(flashers) > 0:
            flash_count += np.sum(flashers)
            octopi[flashers.astype(bool)] = np.nan
            flash_light = convolve2d(flashers, FLASH_MASK, "same")
            octopi += flash_light  # nan values stay nan
            if len(octopi[octopi > 9]) > 0:
                run = True
    np.nan_to_num(octopi, copy=False)  # set nans to 0, inplace
    return octopi, flash_count


def solve_a(puzzle: MyPuzzle):
    answer_a = count_flashing_octopi(puzzle.input_lines, steps=100)
    puzzle.submit_a(answer_a)


def find_flashy_step(inputs: List[str]) -> int:
    octo_x = len(inputs[0])
    octo_y = len(inputs)
    grid_vals = ",".join("".join(inputs)[:])
    octopi = np.fromstring(grid_vals, dtype=float, sep=",").reshape((octo_y, octo_x))

    step = 0
    flashy = False
    while not flashy:
        # assume at step 0 there is no >9 yet
        step += 1
        octopi += 1
        octopi, _ = determine_flashes(octopi)
        if np.all(octopi == 0):
            flashy = True
    return step


def solve_b(puzzle: MyPuzzle):
    answer_b = find_flashy_step(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    solve_b(my_puzzle)
