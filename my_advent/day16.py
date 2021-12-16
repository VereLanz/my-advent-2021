"""
This here is not particularly clean. A colleague made a nicely structured solution:
https://github.com/lukasbindreiter/AdventOfCode2021/blob/main/16/16.ipynb
"""
import math
from typing import Union

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 16

LENGTH_TYPE = {
    "0": 15,  # next 15 bits are total length of bits for all sub-packets
    "1": 11,  # next 11 bits are the number of sub-packets following
}

PACKET_OPERATION = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    4: lambda x: int("".join(x), 2),
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1]),
}


def sum_packet_versions(inputs: list[str]) -> int:
    packets = parse_hex_packs(inputs[0])
    versions = []
    for sub_pack in packets:
        versions.append(int(sub_pack[0], 2))
    return sum(versions)


def parse_hex_packs(hex_code: str) -> list[Union[str, list[str]]]:
    b_codes = []
    for hex_char in hex_code[:]:
        b_codes.append(format(int(hex_char, 16), "04b"))
    b_code = "".join(b_codes)

    packets = []
    # calls itself recursively until all (sub-)packs have been analysed
    parse_next_pack(b_code, packets)
    return packets


def parse_next_pack(b_code: str, packets: list):
    if len(b_code) < 11:
        # all sub-packets have finished, this is padding
        return
    current_pack = [b_code[:3], b_code[3:6]]
    if int(current_pack[1], 2) == 4:  # a literal packet
        i = 0
        while True:
            bits = b_code[6 + 5 * i:6 + 5 * (i + 1)]
            current_pack.append(bits[1:])
            i += 1
            if bits[0] == "0":
                break
        packets.append(current_pack)
        parse_next_pack(b_code[6 + 5 * i:], packets)

    else:  # an operator packet
        length_type_id = b_code[6]
        current_pack.append(length_type_id)
        info_bits_nr = LENGTH_TYPE[length_type_id]
        current_pack.append(b_code[7:7 + info_bits_nr])
        # type "0" -> sub_pack_bits = int(current_pack[-1], 2)  # needed further down
        # type "1" -> sub_pack_nr = int(current_pack[-1], 2)  # needed further down
        packets.append(current_pack)
        parse_next_pack(b_code[7 + info_bits_nr:], packets)


def solve_a(puzzle: MyPuzzle):
    answer_a = sum_packet_versions(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def analyse_packets(inputs: list[str]) -> int:
    packets = parse_hex_packs(inputs[0])
    result = run_packet_operations(packets)
    return result


def run_packet_operations(packets: list[list[str]]) -> int:
    op_types = [int(packet[1], 2) for packet in packets]
    # finding each packets relations that are their operands
    operator_rels = dict()
    all_relations = []
    for i in reversed(range(len(packets))):
        if op_types[i] == 4:
            operator_rels[i] = i
        else:
            operator_rels[i] = find_relations(i, packets, all_relations)

    # running the evaluations of all relations from back to front
    result = evaluate_operations(operator_rels, op_types, packets)
    print(len(packets), len(all_relations), len(set(all_relations)))
    return result


def find_relations(
        i: int, packets: list[list[str]], all_relations: list[int]
) -> list[int]:
    relations = []
    packet_type = packets[i][-2]

    # type "1" gave the number of sub-packets it has
    if packet_type == "1":
        sub_nr = int(packets[i][-1], 2)
        j = i + 1
        while len(relations) < sub_nr:
            if j not in all_relations:
                relations.append(j)
            j += 1

    # type "0" gave the number of bits in it's sub-packets
    elif packet_type == "0":
        sub_bits = int(packets[i][-1], 2)
        packs_len = 0
        j = i + 1
        while j < len(packets):
            packs_len += len("".join(packets[j]))
            if packs_len > sub_bits:
                break
            if j not in all_relations:
                relations.append(j)
            j += 1

    all_relations.extend(relations)
    return relations.copy()


def evaluate_operations(
        operator_rels: dict[int, Union[int, list[int]]], op_types: list[int], packets
) -> int:
    values = dict()
    for i in reversed(range(len(packets))):
        if isinstance(operator_rels[i], int):
            operands = packets[i][2:]
        else:
            # if all can be run in order the values should be available first run
            operands = [values[j] for j in operator_rels[i]]
        values[i] = PACKET_OPERATION[op_types[i]](operands)

    return values[0]  # index 0 is always the last operation


def solve_b(puzzle: MyPuzzle):
    answer_b = analyse_packets(puzzle.input_lines)
    print(answer_b)
    # puzzle.submit_b(answer_b)
    # 18234816433587  NO


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    solve_b(my_puzzle)
