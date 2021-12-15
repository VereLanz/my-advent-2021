import numpy as np
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 15


def find_lowest_risk_path(inputs: list[str]) -> int:
    grid_y = len(inputs)
    grid_x = len(inputs[0])
    matrix = np.fromstring(",".join("".join(inputs)[:]), dtype=int, sep=",").reshape(
        (grid_y, grid_x)
    )

    grid = Grid(matrix=matrix)
    start = grid.node(0, 0)
    end = grid.node(grid_x - 1, grid_y - 1)
    finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
    path, _ = finder.find_path(start, end, grid)

    risk_score = 0
    for step_x, step_y in path[1:]:  # ignore start spot risk score
        risk_score += int(matrix[step_y, step_x])
    return risk_score


def solve_a(puzzle: MyPuzzle):
    answer_a = find_lowest_risk_path(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def find_bigger_lowest_risk_path(inputs: list[str]) -> int:
    big_matrix, max_x, max_y = create_bigger_cave_map(inputs)
    grid = Grid(matrix=big_matrix)
    start = grid.node(0, 0)
    end = grid.node(max_x - 1, max_y - 1)
    finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
    path, _ = finder.find_path(start, end, grid)

    risk_score = 0
    for step_x, step_y in path[1:]:  # ignore start spot risk score
        risk_score += int(big_matrix[step_y, step_x])
    return risk_score


def create_bigger_cave_map(
    inputs: list[str], multi: int = 5
) -> tuple[np.ndarray, int, int]:
    grid_y = len(inputs)
    grid_x = len(inputs[0])
    base_matrix = np.fromstring(
        ",".join("".join(inputs)[:]), dtype=int, sep=","
    ).reshape((grid_y, grid_x))
    big_matrix = np.zeros((grid_y * multi, grid_x * multi))
    mod_matrix = np.ones((grid_y, grid_x)) * 9.1  # risk scores above 9 come back to 1

    for i in range(multi):
        for j in range(multi):
            matrix = np.round(np.mod(base_matrix + i + j, mod_matrix))
            big_matrix[
                grid_y * i: grid_y * (i + 1), grid_x * j: grid_x * (j + 1)
            ] = matrix.copy()
            big_matrix[
                grid_y * j: grid_y * (j + 1), grid_x * i: grid_x * (i + 1)
            ] = matrix.copy()

    return big_matrix, grid_x * multi, grid_y * multi


def solve_b(puzzle: MyPuzzle):
    answer_b = find_bigger_lowest_risk_path(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
