from main.file_reader import read


def solve_1(input: list) -> int:
    ranges = []
    num_fresh = 0
    for i in input:
        if "-" in i:
            start, end = i.split("-")
            ranges.append((int(start), int(end)))
        elif i:
            for start, end in ranges:
                if start <= int(i) <= end:
                    num_fresh += 1
                    break
    return num_fresh


def solve_2(input: list) -> int:
    ranges = []
    for i in input:
        if "-" in i:
            start, end = i.split("-")
            ranges.append((int(start), int(end)))

    num_fresh = 0
    merged_ranges = _merge_ranges(ranges)
    for start, end in merged_ranges:
        num_fresh += end - start + 1

    return num_fresh


def _merge_ranges(ranges: list) -> list:
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged_ranges = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        prev_start, prev_end = merged_ranges[-1]

        if current_start <= prev_end + 1:
            merged_ranges[-1] = (prev_start, max(prev_end, current_end))
        else:
            merged_ranges.append((current_start, current_end))

    return merged_ranges


if __name__ == "__main__":
    input = read("day05-01.txt", "main/year2025/resources")
    print(solve_1(input))  # 690
    print(solve_2(input))  # 344323629240733
