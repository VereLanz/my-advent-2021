from collections import Counter

from my_advent import get_todays_puzzle, MyPuzzle

DAY = 14


def score_full_chain(inputs: list[str], steps: int = 10) -> int:
    chain, rules = parse_input(inputs)
    for _ in range(steps):
        chain_pairs = [chain[i] + chain[i + 1] for i in range(len(chain) - 1)]
        for pair_idx, pair in enumerate(chain_pairs):
            chain_pairs[pair_idx] = pair[0] + rules.get(pair, "") + pair[1]
        new_chain_pieces = [p[:-1] for p in chain_pairs[:-1]]
        chain = "".join(new_chain_pieces) + chain_pairs[-1]
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


def score_full_chain_efficiently(inputs: list[str], steps: int = 40) -> int:
    chain, rules = parse_input(inputs)
    last_letter = chain[-1]
    chain_pairs = [chain[i] + chain[i + 1] for i in range(len(chain) - 1)]
    counter = Counter(chain_pairs)
    for _ in range(steps):
        new_counter = Counter()
        for pair in list(counter.keys()):
            if new_part := rules.get(pair, None):
                new_counter[pair[0] + new_part] += counter[pair]
                new_counter[new_part + pair[1]] += counter[pair]
                del counter[pair]
        counter += new_counter

    # evaluate the resulting chain parts
    letter_counter = Counter()
    for part, number in counter.items():
        letter_counter[part[0]] += number
    letter_counter[last_letter] += 1
    common_letters = letter_counter.most_common()
    chain_score = common_letters[0][1] - common_letters[-1][1]
    return chain_score


def solve_b(puzzle: MyPuzzle):
    answer_b = score_full_chain_efficiently(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
