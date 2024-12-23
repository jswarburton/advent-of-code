from main.year2024.day_22 import solve_1, solve_2


def test_solve_1():
    input = [1, 10, 100, 2024]
    assert solve_1(input) == 37327623


def test_solve_2():
    input = [1, 2, 3, 2024]
    assert solve_2(input) == 23
