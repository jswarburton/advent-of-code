from main.file_reader import read


def solve_1(input: list) -> int:
    total = 0
    for bank in input:
        batteries = [int(battery) for battery in list(bank)]
        total += solve(batteries, max_digits=2)
    return total


def solve_2(input: list) -> int:
    total = 0
    for bank in input:
        batteries = [int(battery) for battery in list(bank)]
        total += solve(batteries, max_digits=12)
    return total


def solve(
    batteries: list, max_digits: int, done: int = 0, agg: int = 0, start_idx: int = 0
) -> int:
    total = 0

    if done == max_digits:
        return agg
    else:
        greedy_idx = start_idx
        for index in range(start_idx, len(batteries) - max_digits + done + 1):
            if batteries[index] > batteries[greedy_idx]:
                greedy_idx = index

        total += solve(
            batteries,
            max_digits,
            done + 1,
            agg * 10 + batteries[greedy_idx],
            greedy_idx + 1,
        )
    return total


if __name__ == "__main__":
    input = read("day03-01.txt", "main/year2025/resources")
    print(solve_1(input))  # 17311
    print(solve_2(input))  # 171419245422055
