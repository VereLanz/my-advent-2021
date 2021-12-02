from typing import List

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 1


def analyse_deepening(scan_report: List[int]) -> int:
    deeper_count = 0
    for i, scan in enumerate(scan_report):
        if i == 0:
            continue
        if scan > scan_report[i - 1]:
            deeper_count += 1
    return deeper_count


def solve_a(puzzle: MyPuzzle):
    answer_a = analyse_deepening(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def group_report_scans(scan_report: List[int]) -> List[int]:
    grouped_scans = []
    for i in range(len(scan_report) - 2):
        # catch that last <three are left out
        try:
            scan_group = sum([scan_report[j] for j in range(i, i + 3)])
            grouped_scans.append(scan_group)
        except IndexError:
            print("scan report grouping finished...")
    return grouped_scans


def solve_b(puzzle: MyPuzzle):
    grouped_scans = group_report_scans(puzzle.input_lines)
    answer_b = analyse_deepening(grouped_scans)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    my_puzzle.input_lines = [int(scan) for scan in my_puzzle.input_lines]
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
