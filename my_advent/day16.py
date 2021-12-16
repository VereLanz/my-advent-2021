import math
from typing import Union

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 16

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

LENGTH_TYPE = {
    "0": 15,  # next 15 bits are total length of bits for all sub-packets
    "1": 11,  # next 11 bits are the number of sub-packets following
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
        next_bits = True
        i = 0
        while next_bits:
            bits = b_code[6 + 5 * i:6 + 5 * (i + 1)]
            current_pack.append(bits[1:])
            i += 1
            if bits[0] == "0":
                next_bits = False
        packets.append(current_pack)
        parse_next_pack(b_code[6 + 5 * i:], packets)

    else:  # an operator packet
        length_type_id = b_code[6]
        current_pack.append(length_type_id)
        info_bits_nr = LENGTH_TYPE[length_type_id]
        current_pack.append(b_code[7:7 + info_bits_nr])
        if length_type_id == "0":
            # sub_pack_bits = int(current_pack[-1], 2)  # not needed?
            packets.append(current_pack)
            parse_next_pack(b_code[7 + info_bits_nr:], packets)
        elif length_type_id == "1":
            # sub_pack_nr = int(current_pack[-1], 2)  # not needed?
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
    operator_rels = {}
    for i, op_type in reversed(list(enumerate(op_types))):
        if op_type != 4:
            relations = []
            for j in range(i + 1, len(op_types)):
                if op_types[j] != 4:
                    break
                relations.append(j)
            if not relations:
                for j in range(i + 1, len(op_types)):
                    if isinstance(operator_rels[j], list):
                        relations.append(j)
                    if packets[i][-2] == "1" and len(relations) == int(packets[i][-1], 2):
                        break
                    # TODO: how to get the correct relations for type 0 operators...
                    # elif packets[i][-2] == "0"
            operator_rels[i] = relations.copy()
        elif op_type == 4:
            operator_rels[i] = PACKET_OPERATION[op_type](packets[i][2:])
    print(operator_rels)

    operators = [(idx, val) for idx, val in operator_rels.items() if isinstance(val, list)]
    while len(operators) > 0:
        print(operators)
        for idx, val in operators:
            run = True
            operands = []
            for op_idx in val:
                operand = operator_rels[op_idx]
                operands.append(operand)
                if isinstance(operand, list):
                    run = False
            if run:
                print(idx, operands, op_types[idx])
                operator_rels[idx] = PACKET_OPERATION[op_types[idx]](operands)
        operators = [(idx, val) for idx, val in operator_rels.items() if isinstance(val, list)]

    return operator_rels[0]  # index 0 is always the last operation


def solve_b(puzzle: MyPuzzle):
    answer_b = analyse_packets(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    solve_b(my_puzzle)
