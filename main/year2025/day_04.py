from main.file_reader import read


def solve_1(input: list) -> int:
    return len(_find_removables(input))


def solve_2(grid: list) -> int:
    total_removed = 0
    while True:
        removables = _find_removables(grid)
        grid = _create_new_grid(grid, removables)
        total_removed += len(removables)

        if not removables:
            break
    return total_removed


def _find_removables(grid: list) -> set:
    removable = set()
    for r, rv in enumerate(grid):
        for c, cv in enumerate(rv):
            if cv == ".":
                continue
            surrounding_values = _get_surrounding_values(grid, r, c)
            num_rolls = surrounding_values.count("@")
            if num_rolls < 4:
                removable.add((r, c))
    return removable


def _get_surrounding_values(grid, row_num, col_num):
    surrounding_values = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr = row_num + dr
            nc = col_num + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[row_num]):
                surrounding_values.append(grid[nr][nc])
    return surrounding_values


def _create_new_grid(grid: list, removables: set) -> list:
    new_grid = []
    for r, rv in enumerate(grid):
        new_row = ""
        for c, cv in enumerate(rv):
            if (r, c) in removables:
                new_row += "."
            else:
                new_row += cv
        new_grid.append(new_row)
    return new_grid


if __name__ == "__main__":
    input = read("day04-01.txt", "main/year2025/resources")
    print(solve_1(input))  # 1435
    print(solve_2(input))  # 8623
