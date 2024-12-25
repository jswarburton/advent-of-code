from main.file_reader import read


def solve_1(input: list) -> int:
    items = []
    item = []
    for i in input:
        if not i:
            items.append(item)
            item = []
        else:
            item.append(i)
    items.append(item)

    locks = []
    keys = []
    for item in items:
        heights = []
        for col in range(len(item[0])):
            height = 0
            for row in range(len(item)):
                if item[row][col] == "#":
                    height += 1
            heights.append(height - 1)
        if item[0][0] == "#":
            locks.append(heights)
        else:
            keys.append(heights)

    count = 0
    for lock_index, item in enumerate(locks):
        for key_index, key in enumerate(keys):
            if all(item[i] <= 5 - key[i] for i in range(len(item))):
                count += 1

    return count


if __name__ == "__main__":
    input = read("day25-01.txt", "main/year2024/resources")
    print(solve_1(input))  # 2691
