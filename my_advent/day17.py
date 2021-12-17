import math

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 17


def shoot_high(inputs: list[str]) -> int:
    target_area = parse_target_area(inputs)
    try_coords = []

    for x, y in try_coords:
        makes_it, max_y = try_shot((x, y), target_area)
        if makes_it:
            return max_y
    return 0


def parse_target_area(inputs: list[str]) -> dict[str, range]:
    x_area, y_area = inputs[0].replace("target area: ", "").split(", ")
    x_min, x_max = x_area.replace("x=", "").split("..")
    y_min, y_max = y_area.replace("y=", "").split("..")
    return {"x_range": range(int(x_min), int(x_max) + 1),
            "y_range": range(int(y_min), int(y_max) + 1)}


def find_x_for_steps(steps: int, target_x: range) -> int:
    # we'll aim for near minimum in general to get a high y (needs a few steps)
    min_x = list(target_x)[0]
    mean_x_vel = min_x / steps
    start_x = round(mean_x_vel + steps / 2)
    drag = steps * start_x - sum(range(steps)) if start_x >= (steps - 1) else 0  # TODO
    assert start_x * steps - drag in target_x
    return start_x


def find_highest_y_steps(target_y: range) -> tuple[int, int]:
    # we'll just define a plausible range
    pass


def try_shot(
    start_velocity: tuple[int, int], steps: int, target_area: dict[str, range]
) -> tuple[bool, int]:
    pass


def solve_a(puzzle: MyPuzzle):
    answer_a = shoot_high(puzzle.input_lines)
    # puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = (puzzle.input_lines)
    # puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
