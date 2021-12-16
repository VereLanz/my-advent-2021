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
    5: lambda x, y: int(x > y),
    6: lambda x, y: int(x < y),
    7: lambda x, y: int(x == y),
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
    print(packets)
    return packets


def parse_next_pack(b_code: str, packets: list):
    print(b_code)
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


def run_packet_operations(inputs: list[str]) -> int:
    packets = parse_hex_packs(inputs[0])
    result = analyse_packet_operations(packets)
    return result


def analyse_packet_operations(packets: list[list[str]]) -> int:
    # TODO: group packets and run PACKET_OPERATION functions in order (inner to outer)
    pass


def solve_b(puzzle: MyPuzzle):
    answer_b = run_packet_operations(puzzle.input_lines)
    # puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    solve_b(my_puzzle)
