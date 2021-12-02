from typing import List

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 2


class Submarine:
    x = 0
    depth = 0
    aim = 0

    # for Part One
    @classmethod
    def move_forward(cls, x: int):
        cls.x += x

    @classmethod
    def move_down(cls, y: int):
        cls.depth += y

    @classmethod
    def move_up(cls, y: int):
        cls.depth -= y

    # for Part Two
    @classmethod
    def aim_forward(cls, x: int):
        cls.x += x
        cls.depth += cls.aim * x

    @classmethod
    def aim_down(cls, y: int):
        cls.aim += y

    @classmethod
    def aim_up(cls, y: int):
        cls.aim -= y


MOVEMENT_MAP_ONE = {
    "forward": Submarine.move_forward,
    "down": Submarine.move_down,
    "up": Submarine.move_up,
}

MOVEMENT_MAP_TWO = {
    "forward": Submarine.aim_forward,
    "down": Submarine.aim_down,
    "up": Submarine.aim_up,
}


def move_submarine_path(inputs: List[str]):
    for move_input in inputs:
        direction, amount = move_input.split()
        MOVEMENT_MAP_ONE[direction](int(amount))
    return Submarine.x * Submarine.depth


def solve_a(puzzle: MyPuzzle):
    answer_a = move_submarine_path(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def move_submarine_with_aim(inputs: list[str]):
    for move_input in inputs:
        direction, amount = move_input.split()
        MOVEMENT_MAP_TWO[direction](int(amount))
    return Submarine.x * Submarine.depth


def solve_b(puzzle: MyPuzzle):
    answer_b = move_submarine_with_aim(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
