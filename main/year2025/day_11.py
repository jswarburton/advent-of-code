from functools import cache

from main.file_reader import read


def solve_1(input: list) -> int:
    devices = dict()
    for i in input:
        a, b = i.split(": ")
        devices[a] = b.split()

    @cache
    def solve(node):
        if node == "out":
            return 1

        return sum(solve(neighbour) for neighbour in devices[node])

    return solve("you")


def solve_2(input: list) -> int:
    devices = dict()
    for i in input:
        a, b = i.split(": ")
        devices[a] = b.split()

    @cache
    def solve(node, dac, fft):
        if node == "out":
            return 1 if dac and fft else 0

        return sum(
            solve(neighbour, dac or neighbour == "dac", fft or neighbour == "fft")
            for neighbour in devices[node]
        )

    return solve("svr", False, False)


if __name__ == "__main__":
    input = read("day11-01.txt", "main/year2025/resources")
    print(solve_1(input))  # 470
    print(solve_2(input))  # 384151614084875
