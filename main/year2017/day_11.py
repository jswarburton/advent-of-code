from main.file_reader import read

directions = {
    "n": (0, 1, -1),
    "ne": (1, 0, -1),
    "se": (1, -1, 0),
    "s": (0, -1, 1),
    "sw": (-1, 0, 1),
    "nw": (-1, 1, 0),
}


def solve_1(input: str) -> int:
    x, y, z = 0, 0, 0

    for step in input.split(","):
        dx, dy, dz = directions[step]
        x += dx
        y += dy
        z += dz

    distance = (abs(x) + abs(y) + abs(z)) // 2

    return distance


def solve_2(input: str) -> int:
    x, y, z = 0, 0, 0
    max_dist = 0

    for step in input.split(","):
        dx, dy, dz = directions[step]
        x += dx
        y += dy
        z += dz

        distance = (abs(x) + abs(y) + abs(z)) // 2
        if distance > max_dist:
            max_dist = distance

    return max_dist


if __name__ == "__main__":
    input = read("day11-01.txt", "main/year2017/resources")[0]
    print(solve_1(input))  # 812
    print(solve_2(input))  # 1603
