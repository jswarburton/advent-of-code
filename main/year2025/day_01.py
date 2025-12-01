from main.file_reader import read


def solve_1(input: list) -> int:
    pos = 50
    count = 0

    for i in input:
        dir = i[0]
        dis = int(i[1:])

        if dir == "L":
            pos -= dis
        elif dir == "R":
            pos += dis

        pos %= 100
        if pos < 0:
            pos += 100
        elif pos >= 100:
            pos -= 100

        if pos == 0:
            count += 1

    return count


def solve_2(input: list) -> int:
    pos = 50
    count = 0

    for i in input:
        dir = i[0]
        dis = int(i[1:])

        count += dis // 100
        dis %= 100

        if dir == "L":
            pos -= dis
            if pos < 0:
                if pos + dis != 0:
                    count += 1
                pos += 100
            if pos == 0:
                count += 1
        elif dir == "R":
            pos += dis
            if pos > 99:
                if pos - dis != 0:
                    count += 1
                pos -= 100

    return count


if __name__ == "__main__":
    input = read("day01-01.txt", "main/year2025/resources")
    print(solve_1(input))  # 1089
    print(solve_2(input))  # 6530
