from collections import deque

from z3 import Int, Optimize

from main.file_reader import read


def solve_1(input: list) -> int:
    total = 0
    for i in input:
        parts = i.split()
        indicator_lights = set(i for i, x in enumerate(parts[0][1:-1]) if x == "#")
        buttons = [set(map(int, p[1:-1].split(","))) for p in parts[1:-1]]

        total += bfs(indicator_lights, buttons)
    return total


def bfs(target, buttons):
    q = deque()
    q.append((set(), 0))
    seen_states = set()
    while q:
        curr_state, steps = q.popleft()
        if curr_state == target:
            return steps
        for button in buttons:
            new_state = curr_state ^ button
            if new_state in seen_states:
                continue
            seen_states.add(frozenset(new_state))
            q.append((new_state, steps + 1))


def solve_2(input: list) -> int:
    total = 0
    for i in input:
        parts = i.split()
        joltage = [int(p) for p in parts[-1][1:-1].split(",")]
        buttons = [set(map(int, p[1:-1].split(","))) for p in parts[1:-1]]

        total += find_min_presses(joltage, buttons)
    return total


def find_min_presses(target_joltage, buttons):
    opt = Optimize()

    button_presses = [Int(f"button_{i}") for i in range(len(buttons))]

    for press in button_presses:
        opt.add(press >= 0)

    num_counters = len(target_joltage)
    for counter_idx in range(num_counters):
        contributions = []
        for button_idx, button in enumerate(buttons):
            if counter_idx in button:
                contributions.append(button_presses[button_idx])

        if contributions:
            opt.add(sum(contributions) == target_joltage[counter_idx])
        else:
            opt.add(target_joltage[counter_idx] == 0)

    opt.minimize(sum(button_presses))

    opt.check()
    model = opt.model()
    total_presses = sum(model[press].as_long() for press in button_presses)
    return total_presses


if __name__ == "__main__":
    input = read("day10-01.txt", "main/year2025/resources")
    print(solve_1(input))  # 475
    print(solve_2(input))  # 18273
