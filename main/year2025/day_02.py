from main.file_reader import read


def solve_1(input: list) -> int:
    total = 0
    a = input[0].split(",")
    for j in a:
        start, end = j.split("-")
        start = int(start)
        end = int(end)

        for k in range(start, end + 1):
            str_k = str(k)
            if str_k[: len(str_k) // 2] == str_k[len(str_k) // 2 :]:
                total += k

    return total


def solve_2(input: list) -> int:
    total = 0
    a = input[0].split(",")
    for j in a:
        start, end = j.split("-")
        start = int(start)
        end = int(end)

        for k in range(start, end + 1):
            str_k = str(k)
            n = len(str_k)

            for pattern_len in range(1, n):
                if n % pattern_len == 0:
                    pattern = str_k[:pattern_len]
                    if pattern * (n // pattern_len) == str_k:
                        total += k
                        break

    return total


if __name__ == "__main__":
    input = read("day02-01.txt", "main/year2025/resources")
    print(solve_1(input))  # 30608905813
    print(solve_2(input))  # 31898925685
