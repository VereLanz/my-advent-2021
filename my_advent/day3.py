from collections import Counter
from typing import List

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 3


def calculate_power_consumption(inputs: List[str]) -> int:
    gamma = ""
    epsilon = ""
    # it's safe to assume every element has the same length
    for i in range(len(inputs[0])):
        position_bits = "".join([bits[i] for bits in inputs])
        bit_commons = Counter(position_bits).most_common(2)
        gamma += bit_commons[0][0]
        epsilon += bit_commons[1][0]
    return int(gamma, 2) * int(epsilon, 2)


def solve_a(puzzle: MyPuzzle):
    answer_a = calculate_power_consumption(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def calculate_life_support(inputs: List[str]) -> int:
    # O2 part, keep most common or 1
    o2_values = [inputs]
    i = 0
    while i < len(inputs[0]) and len(o2_values[-1]) != 1:
        position_bits = "".join([bits[i] for bits in o2_values[i]])
        bit_commons = Counter(position_bits).most_common(2)
        keep = bit_commons[0][0]
        if bit_commons[0][1] == bit_commons[1][1]:
            keep = "1"
        o2_values.append([bits for bits in o2_values[i] if bits[i] == keep])
        i += 1

    if len(o2_values[-1]) == 1:
        o2_gen = o2_values[-1][0]
    else:
        o2_gen = ""
        for i in range(len(inputs[0])):
            position_bits = "".join([bits[i] for bits in o2_values[-1]])
            bit_commons = Counter(position_bits).most_common(2)
            o2_gen += bit_commons[0][0]

    # CO2 part, keep least common or 0
    co2_values = [inputs]
    i = 0
    while i < len(inputs[0]) and len(co2_values[-1]) != 1:
        position_bits = "".join([bits[i] for bits in co2_values[i]])
        bit_commons = Counter(position_bits).most_common(2)
        keep = bit_commons[1][0]
        if bit_commons[0][1] == bit_commons[1][1]:
            keep = "0"
        co2_values.append([bits for bits in co2_values[i] if bits[i] == keep])
        i += 1

    if len(co2_values[-1]) == 1:
        co2_scrub = co2_values[-1][0]
    else:
        co2_scrub = ""
        for i in range(len(inputs[0])):
            position_bits = "".join([bits[i] for bits in co2_values[-1]])
            bit_commons = Counter(position_bits).most_common(2)
            co2_scrub += bit_commons[1][0]

    return int(o2_gen, 2) * int(co2_scrub, 2)


def solve_b(puzzle: MyPuzzle):
    answer_b = calculate_life_support(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    solve_b(my_puzzle)
