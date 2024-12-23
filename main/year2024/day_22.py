from collections import defaultdict

from main.file_reader import read


def solve_1(input: list) -> int:
    return sum(generate_secret_number(int(i)) for i in input)


def solve_2(input: list) -> int:
    seqs = defaultdict(int)

    for line in input:
        n = int(line)
        results = []
        for _ in range(2000):
            start = n % 10
            n = generate_secret_number(n, steps=1)
            results.append((n, (n % 10) - start))

        seqs_this_round = set()
        for i in range(0, len(results) - 3):
            seq = tuple([results[i + j][1] for j in range(4)])
            if seq not in seqs_this_round:
                seqs[seq] += results[i + 3][0] % 10
                seqs_this_round.add(seq)

    return max(seqs.values())


def generate_secret_number(initial_number, steps=2000):
    def prune(number):
        return number % 16777216

    def mix(number, value):
        return number ^ value

    secret_number = initial_number
    for _ in range(steps):
        secret_number = prune(mix(secret_number, secret_number * 64))
        secret_number = prune(mix(secret_number, secret_number // 32))
        secret_number = prune(mix(secret_number, secret_number * 2048))

    return secret_number


if __name__ == "__main__":
    input = read("day22-01.txt", "main/year2024/resources")
    print(solve_1(input))  # 15303617151
    print(solve_2(input))  # 1727
