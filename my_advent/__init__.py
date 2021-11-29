# utils for doing advent of code
from typing import Any

from aocd.models import Puzzle


def get_today(day: int, year: int = 2021):
    puzzle = Puzzle(year=year, day=day)
    input_lines = puzzle.input_data.splitlines()
    return puzzle, input_lines


# i just prefer submitting via function, not as setting an attribute...
def submit_a(puzzle: Puzzle, answer: Any):
    puzzle.answer_a = answer


def submit_b(puzzle: Puzzle, answer: Any):
    puzzle.answer_b = answer
