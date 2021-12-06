from collections import Counter
from typing import List

import numpy as np

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 6


def calculate_spawns(inputs: List[str], days: int) -> int:
    """
    NOTE: this function does no longer work for too many days or fish! :P
    """
    start_timers = np.array(inputs[0].split(","), dtype=int)
    # rough (overshooting) estimate for max array size to avoid appending
    max_fish = int(len(start_timers) * (2 ** (days / 7.8)))
    spawn_timers = np.zeros(max_fish) - 2
    spawn_timers[:len(start_timers)] = start_timers

    for _ in range(days):
        # pass a day for existing fish
        spawn_timers[spawn_timers != -2] -= 1
        # check if any are at -1, if yes -> set it to 6, add an 8 (= fresh spawn)
        spawners = len(spawn_timers[spawn_timers == -1])
        if spawners > 0:
            spawn_timers[spawn_timers == -1] = 6
            current_fish = len(spawn_timers[spawn_timers != -2])
            spawn_timers[current_fish:current_fish + spawners] = 8

    lanternfish = len(spawn_timers[spawn_timers != -2])
    return lanternfish


def calculate_massive_spawns(inputs: List[str], days: int) -> int:
    start_timers = [int(i) for i in inputs[0].split(",")]
    # spawn timer: amount of fish with that timer
    population = {i: 0 for i in range(8, -1, -1)}
    population.update(Counter(start_timers))

    for _ in range(days):
        population = update_population(population)

    amount_of_fish = sum(population.values())
    return amount_of_fish


def update_population(population):
    new_population = {k - 1: v for k, v in population.items()}
    offspring = new_population.pop(-1)
    new_population[6] += offspring
    new_population[8] = offspring
    return new_population


def solve_a(puzzle: MyPuzzle):
    answer_a = calculate_spawns(puzzle.input_lines, days=80)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = calculate_massive_spawns(puzzle.input_lines, days=256)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    solve_b(my_puzzle)
