from my_advent import get_todays_puzzle, MyPuzzle

DAY = 12


def count_paths_through_system(inputs: list[str]) -> int:
    path_connections = map_path_connections(inputs)
    all_paths = []
    search_possible_paths(path_connections, "start", [], all_paths)
    sensible_paths = [p for p in all_paths if p[-1] == "end"]
    return len(sensible_paths)


def map_path_connections(inputs: list[str]) -> dict:
    path_connections = dict()
    single_conns = sorted([line.split("-") for line in inputs])
    caves = list(set([c for conn in single_conns for c in conn]))
    for cave in caves:
        rel_conns = [c for c in single_conns if cave in c]
        conns = [c for conn in rel_conns for c in conn if c != cave]
        path_connections[cave] = conns
    return path_connections


def search_possible_paths(
    connections: dict[str, list[str]],
    current: str,
    visited: list[str],
    all_paths: list[list[str]],
):
    """
    Recursive depth first search with one defined end point ("end") and
    some multiple visits allowed (uppercase), some not (lowercase).
    """
    visited.append(current)
    for conn in connections[current]:
        if conn == "end":
            visited.append(conn)
            continue
        if (conn.islower() and conn not in visited) or conn.isupper():
            search_possible_paths(connections, conn, visited.copy(), all_paths)
    all_paths.append(visited)


def solve_a(puzzle: MyPuzzle):
    answer_a = count_paths_through_system(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = puzzle.input_lines
    # puzzle.submit_b(answer_b)


if __name__ == "__main__":
    my_puzzle = get_todays_puzzle(DAY)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
