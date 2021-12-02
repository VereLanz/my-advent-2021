# utils for doing advent of code
from typing import Any

from aocd.models import Puzzle


class MyPuzzle(Puzzle):
    def __init__(self, year: int, day: int):
        super().__init__(year=year, day=day)
        self.input_lines = self.input_data.splitlines()

    def submit_a(self, answer: Any):
        self.answer_a = answer

    def submit_b(self, answer: Any):
        self.answer_b = answer


def get_todays_puzzle(day: int, year: int = 2021):
    my_puzzle = MyPuzzle(year=year, day=day)
    return my_puzzle
