from my_advent.day1 import analyse_deepening, group_report_scans


def test_example_a():
    example_input = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]
    example_result = 7  # measurements are larger than the previous
    assert analyse_deepening(example_input) == example_result


def test_example_b():
    example_input = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]
    example_result = 5  # measurement groups are larger than the previous
    grouped_scans = group_report_scans(example_input)
    assert analyse_deepening(grouped_scans) == example_result
