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


def solve_b(puzzle: MyPuzzle):
    # answer_b = (puzzle.input_lines)
    # puzzle.submit_b(answer_b)
    pass


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
