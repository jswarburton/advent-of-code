from main.year2025.day_03 import solve_1, solve_2

input = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]


def test_solve_1():
    assert solve_1(input) == 357


def test_solve_2():
    assert solve_2(input) == 3121910778619
