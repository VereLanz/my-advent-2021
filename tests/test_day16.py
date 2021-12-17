import pytest

from my_advent.day16 import sum_packet_versions, analyse_packets


@pytest.mark.parametrize(
    ("hex_input", "result"),
    [
        (["D2FE28"], 6),
        (["38006F45291200"], 1 + 6 + 2),  # 9
        (["EE00D40C823060"], 7 + 2 + 4 + 1),  # 14
        (["8A004A801A8002F478"], 16),
        (["620080001611562C8802118E34"], 12),
        (["C0015000016115A2E0802F182340"], 23),
        (["A0016C880162017C3686B18A3D4780"], 31),
    ]
)
def test_example_a(hex_input, result):
    assert sum_packet_versions(hex_input) == result


@pytest.mark.parametrize(
    ("hex_input", "result"),
    [
        (["D2FE28"], 2021),
        (["C200B40A82"], 3),
        (["04005AC33890"], 54),
        (["880086C3E88112"], 7),
        (["CE00C43D881120"], 9),
        (["D8005AC2A8F0"], 1),
        (["F600BC2D8F"], 0),
        (["9C005AC2F8F0"], 0),
        (["9C0141080250320F1802104A08"], 1),
        (["000294200841022044088110220440881102204408811020"], 2),  # thx reddit helper!
    ]
)
def test_example_b(hex_input, result):
    assert analyse_packets(hex_input) == result
