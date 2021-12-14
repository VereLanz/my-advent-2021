from collections import Counter

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 14


def score_full_chain(inputs: list[str], steps: int = 10) -> int:
    chain, rules = parse_input(inputs)
    for _ in range(steps):
        chain_pairs = [chain[i] + chain[i + 1] for i in range(len(chain) - 1)]
        new_chain_sets = chain_pairs.copy()
        for pair_idx, pair in enumerate(chain_pairs):
            if pair in rules.keys():
                new_chain_sets[pair_idx] = pair[0] + rules[pair] + pair[1]
        new_chain_pieces = [p[:-1] for p in new_chain_sets[:-1]]
        new_chain_pieces.append(new_chain_sets[-1])
        chain = "".join(new_chain_pieces)
    counter = Counter(chain).most_common()
    chain_score = counter[0][1] - counter[-1][1]
    return chain_score


def parse_input(inputs: list[str]) -> tuple[str, dict[str, str]]:
    chain, rules = "\n".join(inputs).split("\n\n")
    rules = [tuple(r.split(" -> ")) for r in rules.splitlines()]
    rules = dict(rules)
    return chain.strip(), rules


def solve_a(puzzle: MyPuzzle):
    answer_a = score_full_chain(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = (puzzle.input_lines)
    # puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    solve_a(my_puzzle)
    # solve_b(my_puzzle)
