import math

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 17


def shoot_high(inputs: list[str]) -> int:
    target_area = parse_target_area(inputs)

    highest_y = find_highest_y(target_area["y_range"])
    steps = find_steps_for_y(highest_y)
    good_x = find_x_for_steps(steps, target_area["x_range"])

    makes_it, max_y = try_shot((good_x, highest_y), steps, target_area)
    if makes_it:
        return max_y
    return 0


def parse_target_area(inputs: list[str]) -> dict[str, range]:
    x_area, y_area = inputs[0].replace("target area: ", "").split(", ")
    x_min, x_max = x_area.replace("x=", "").split("..")
    y_min, y_max = y_area.replace("y=", "").split("..")
    return {"x_range": range(int(x_min), int(x_max) + 1),
            "y_range": range(int(y_min), int(y_max) + 1)}


def find_highest_y(target_y: range) -> int:
    highest_possible_y = list(target_y)[-1]
    pass


def find_x_for_steps(steps: int, target_x: range) -> int:
    # we'll aim for near minimum in general to get a high y (needs a few steps)
    min_x = list(target_x)[0]
    mean_x_vel = min_x / steps
    start_x = round(mean_x_vel + steps / 2)
    if start_x < steps:
        drag = sum(range(start_x)) + (steps - start_x) * start_x
    else:
        drag = sum(range(steps))
    assert start_x * steps - drag in target_x
    return start_x


def find_steps_for_y(y: int) -> int:
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
