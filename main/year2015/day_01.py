from main.file_reader import read


def solve_1(input: str) -> int:
    count = 0
    for i in input:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
    return count


def solve_2(input: str) -> int:
    count = 0
    for i, v in enumerate(input):
        if v == "(":
            count += 1
        elif v == ")":
            count -= 1
        if count < 0:
            return i + 1


if __name__ == "__main__":
    input = read("day01-01.txt", "main/year2015/resources")[0]
    print(solve_1(input))  # 280
    print(solve_2(input))  # 1797
