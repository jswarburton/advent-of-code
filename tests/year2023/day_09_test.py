from main import file_reader
from main.year2023.day_09 import solve_1, solve_2

input = file_reader.read(file_name="day09.txt", path="tests/year2023/resources")


def test_solve_1():
    assert solve_1(input) == 114


def test_solve_2():
    assert solve_2(input) == 2