from typing import List, Tuple

import numpy as np
from numpy.ma.core import MaskedArray

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 4


def find_first_bingo_score(inputs: List[str]) -> int:
    win_sum = 0
    win_number = 0

    draw_numbers, boards = parse_input(inputs)

    bingo = False
    for drawn in draw_numbers:
        # every draw check each board for bingo (assume in order is okay)
        for b_idx in range(len(boards)):  # to change the boards inside every loop
            # mask drawn number on each board then check if that bingoed
            boards[b_idx] = np.ma.masked_where(boards[b_idx] == drawn, boards[b_idx])
            bingo = check_bingo(boards[b_idx])
            if bingo:
                win_sum = np.sum(boards[b_idx])  # mask is active
                win_number = drawn
                break
        if bingo:
            break

    return win_sum * win_number


def parse_input(inputs: List[str]) -> Tuple[List[int], List[MaskedArray]]:
    input_parts = "\n".join(inputs).split("\n\n")
    draw_numbers = [int(i) for i in input_parts[0].split(",")]

    # assume every board has the same shape
    board_lines = input_parts[1].split("\n")
    board_shape = (len(board_lines), len(board_lines[0].split()))
    boards = []
    for board_line in input_parts[1:]:
        board = np.fromstring(board_line, dtype=int, sep=" ").reshape(board_shape)
        boards.append(np.ma.array(board))

    return draw_numbers, boards


def check_bingo(board: MaskedArray) -> bool:
    try:  # faster than checking every check if there is a mask first
        if np.any([np.all(line) for line in board.mask]) or np.any(
            [np.all(tline) for tline in board.mask.T]
        ):
            return True
    except TypeError:
        # before any value was masked board.mask is just False, not iterable
        # but if it's a mask you cannot check it's truth value
        pass
    return False


def solve_a(puzzle: MyPuzzle):
    answer_a = find_first_bingo_score(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def find_last_bingo_score(inputs: List[str]) -> int:
    lose_sum = 0
    lose_number = 0

    draw_numbers, boards = parse_input(inputs)

    bingo_count = 0
    board_count = len(boards)
    bingo_blacklist = []
    for drawn in draw_numbers:
        # every draw check each board for bingo (assume in order is okay)
        for b_idx in range(board_count):
            if b_idx in bingo_blacklist:
                # don't check boards that have already bingoed
                continue
            # mask drawn number on each board then check if that bingoed
            boards[b_idx] = np.ma.masked_where(boards[b_idx] == drawn, boards[b_idx])
            bingo = check_bingo(boards[b_idx])
            if bingo:
                bingo_count += 1
                bingo_blacklist.append(b_idx)
            if bingo_count == board_count:
                lose_sum = np.sum(boards[b_idx])  # mask is active
                lose_number = drawn
                break

        if bingo_count == board_count:
            # the last one bingoed
            break

    return lose_sum * lose_number


def solve_b(puzzle: MyPuzzle):
    answer_b = find_last_bingo_score(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
