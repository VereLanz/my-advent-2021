from typing import List

from my_advent import *

DAY = 1


def analyse_deepening(scan_report: List[int]) -> int:
    deeper_count = 0
    for i, scan in enumerate(scan_report):
        if i == 0:
            continue
        if scan > scan_report[i - 1]:
            deeper_count += 1
    return deeper_count


def solve_a(puzzle, inp):
    answer_a = analyse_deepening(inp)
    submit_a(puzzle, answer_a)


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


def solve_b(puzzle, inp):
    grouped_scans = group_report_scans(inp)
    answer_b = analyse_deepening(grouped_scans)
    submit_b(puzzle, answer_b)


if __name__ == "__main__":
    puzzle_obj, inp_list = get_today(DAY)
    inp_list = [int(scan) for scan in inp_list]
    # solve_a(puzzle_obj, inp_list)
    # solve_b(puzzle_obj, inp_list)
