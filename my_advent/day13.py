import numpy as np

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 13


def fold_and_count_dots(inputs: list[str]) -> int:
    points, instructions = parse_origami_input(inputs)
    # create np sheet
    sheet_x = max([p[0] for p in points]) + 1
    sheet_y = max([p[1] for p in points]) + 1
    sheet = np.zeros((sheet_y, sheet_x))
    for x, y in points:
        sheet[y][x] = 1
    for coord, line_idx in instructions[:1]:  # part a only needs the first instruction
        sheet = fold_origami_sheet(sheet, coord, int(line_idx))
    return int(np.sum(sheet))


def parse_origami_input(
    inputs: list[str],
) -> tuple[list[tuple[int, int]], list[list[str]]]:
    points, instructions = "\n".join(inputs).split("\n\n")
    points = [(int(p.split(",")[0]), int(p.split(",")[1])) for p in points.splitlines()]
    instructions = [
        s.replace("fold along ", "").split("=") for s in instructions.splitlines()
    ]
    return points, instructions


def fold_origami_sheet(sheet: np.ndarray, coord: str, line_idx: int) -> np.ndarray:
    if coord == "x":  # vertical fold
        sheet = sheet.T
    # (simulated) horizontal fold
    top = sheet[:line_idx].copy()
    bottom = sheet[line_idx + 1:].copy()
    top[-1 * len(bottom):] += bottom[::-1]
    sheet = top.copy()
    sheet[sheet > 1] = 1
    if coord == "x":
        sheet = sheet.T
    return sheet


def solve_a(puzzle: MyPuzzle):
    answer_a = fold_and_count_dots(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def fold_and_show_dots(inputs: list[str]):
    points, instructions = parse_origami_input(inputs)
    # create np sheet
    sheet_x = max([p[0] for p in points]) + 1
    sheet_y = max([p[1] for p in points]) + 1
    sheet = np.zeros((sheet_y, sheet_x))
    for x, y in points:
        sheet[y][x] = 1
    for coord, line_idx in instructions:
        sheet = fold_origami_sheet(sheet, coord, int(line_idx))
    print(sheet)


def solve_b(puzzle: MyPuzzle):
    fold_and_show_dots(puzzle.input_lines)
    # it shows ALREKFKU
    puzzle.submit_b("ALREKFKU")


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
