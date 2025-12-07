from main.file_reader import read


def solve_1(input: list) -> int:
    start = None
    for row_num, i in enumerate(input):
        for col_num, j in enumerate(i):
            if input[row_num][col_num] == "S":
                start = (row_num, col_num)

    beam_positions = set()
    beam_positions.add(start)

    splits = 0

    for _ in range(len(input) - 1):
        new_beam_positions = set()
        for beam_row, beam_col in beam_positions:
            if input[beam_row + 1][beam_col] == "^":
                new_beam_positions.add((beam_row + 1, beam_col - 1))
                new_beam_positions.add((beam_row + 1, beam_col + 1))
                splits += 1
            else:
                new_beam_positions.add((beam_row + 1, beam_col))
        beam_positions = new_beam_positions
    return splits


def solve_2(input: list) -> int:
    start = None
    for row_num, i in enumerate(input):
        for col_num, j in enumerate(i):
            if input[row_num][col_num] == "S":
                start = (row_num, col_num)

    beam_positions = dict()
    beam_positions[start] = 1

    for _ in range(len(input) - 1):
        new_beam_positions = dict()
        for (beam_row, beam_col), count in beam_positions.items():
            if input[beam_row + 1][beam_col] == "^":
                new_beam_positions[(beam_row + 1, beam_col - 1)] = (
                    new_beam_positions.get((beam_row + 1, beam_col - 1), 0) + count
                )
                new_beam_positions[(beam_row + 1, beam_col + 1)] = (
                    new_beam_positions.get((beam_row + 1, beam_col + 1), 0) + count
                )
            else:
                new_beam_positions[(beam_row + 1, beam_col)] = (
                    new_beam_positions.get((beam_row + 1, beam_col), 0) + count
                )
        beam_positions = new_beam_positions
    return sum(beam_positions.values())


if __name__ == "__main__":
    input = read("day07-01.txt", "main/year2025/resources")
    print(solve_1(input))  # 1703
    print(solve_2(input))  # 171692855075500
