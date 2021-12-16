from typing import Union

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 16

PACKET_TYPE = {
    0: "operator",  # everything else than 4 atm
    4: "literal",
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
    # if padding needed: format(int(hex, 16), "04b"); 04 is padding to 4 with 0s
    b_code = bin(int(hex_code, 16))[2:]
    packets = []

    # calls itself recursively until all (sub-)packs have been analysed
    parse_next_pack(b_code, packets)
    print(packets)
    return packets


def parse_next_pack(b_code: str, packets: list):
    if len(b_code) < 11:
        # all sub-packets have finished, this is padding
        return
    current_pack = [b_code[:3], b_code[3:6]]
    if int(current_pack[1], 2) == 4:  # a literal packet, no further sub-packets
        for i in range(int(len(b_code[6:]) / 5)):  # works if the rest-bits are < 5
            current_pack.append(b_code[6 + 5 * i:6 + 5 * (i + 1)][1:])
        packets.append(current_pack)

    else:  # an operator packet
        length_type_id = b_code[6]
        current_pack.append(length_type_id)
        info_bits_nr = LENGTH_TYPE[length_type_id]
        current_pack.append(b_code[7:7 + info_bits_nr])
        if length_type_id == "0":
            sub_pack_bits = int(current_pack[-1], 2)
            packets.append(current_pack)
            parse_next_pack(b_code[7 + info_bits_nr:7 + info_bits_nr + sub_pack_bits], packets)
        elif length_type_id == "1":
            # sub_pack_nr = int(current_pack[-1], 2)  # not needed?
            packets.append(current_pack)
            parse_next_pack(b_code[7 + info_bits_nr:], packets)


def solve_a(puzzle: MyPuzzle):
    answer_a = sum_packet_versions(puzzle.input_lines)
    # puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = (puzzle.input_lines)
    # puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
