from my_advent import get_todays_puzzle, MyPuzzle

DAY = 17


def shoot_high(inputs: list[str]) -> int:
    target_area = parse_target_area(inputs)

    highest_y_start = abs(min(target_area["y_range"])) - 1
    max_y = sum(range(highest_y_start + 1))

    return max_y


def parse_target_area(inputs: list[str]) -> dict[str, range]:
    x_area, y_area = inputs[0].replace("target area: ", "").split(", ")
    x_min, x_max = x_area.replace("x=", "").split("..")
    y_min, y_max = y_area.replace("y=", "").split("..")
    return {"x_range": range(int(x_min), int(x_max) + 1),
            "y_range": range(int(y_min), int(y_max) + 1)}


def find_x_for_steps(steps: int, target_x: range) -> int:
    # we'll aim for near minimum first
    min_x = list(target_x)[0]
    mean_x_vel = min_x / steps
    start_x = round(mean_x_vel + steps / 2)
    return start_x


def solve_a(puzzle: MyPuzzle):
    answer_a = shoot_high(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def find_all_shots(inputs: list[str]) -> int:
    target_area = parse_target_area(inputs)
    good_shots = []
    for y in range(min(target_area["y_range"]), abs(min(target_area["y_range"]))):
        # TODO: how to get general steps?
        if y > 0:
            steps = 0
        else:
            steps = 0
        x = find_x_for_steps(steps, target_area["x_range"])
        good = try_shot(x, y, steps, target_area)
        if good:
            good_shots.append((x, y))
    return len(good_shots)


def try_shot(x: int, y: int, steps: int, target_area: dict[str, range]) -> bool:
    if x < steps:
        drag = sum(range(x)) + (steps - x) * x
    else:
        drag = sum(range(steps))
    x_good = x * steps - drag in target_area["x_range"]

    # TODO: whole y good check part
    if y > 0:
        y_good = False

    if x_good and y_good:
        return True
    return False


def solve_b(puzzle: MyPuzzle):
    answer_b = find_all_shots(puzzle.input_lines)
    # puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    solve_b(my_puzzle)
