import pytest

from my_advent.day16 import sum_packet_versions

EXAMPLE_INPUT = [
    "D2FE28",  # example_result = 2021
]


@pytest.mark.parametrize(
    ("hex_input", "result"),
    [
        (["D2FE28"], 6),
        (["8A004A801A8002F478"], 16),
        (["620080001611562C8802118E34"], 12),
        (["C0015000016115A2E0802F182340"], 23),
        (["A0016C880162017C3686B18A3D4780"], 31),
    ]
)
def test_example_a(hex_input, result):
    assert sum_packet_versions(hex_input) == result


def test_example_b():
    example_result = 0
    assert a(EXAMPLE_INPUT) == example_result
