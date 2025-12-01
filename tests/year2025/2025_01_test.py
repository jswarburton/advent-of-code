from main.year2025.day_01 import solve_1, solve_2

input = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]


def test_solve_1():
    assert solve_1(input) == 3


def test_solve_2():
    assert solve_2(input) == 6
