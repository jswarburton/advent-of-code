from main import file_reader
from main.day_02 import solve_1, solve_2

input = file_reader.read(file_name="day02.txt", path="tests/resources")


def test_solve_1():
    assert solve_1(input) == 8


def test_solve_2():
    assert solve_2(input) == 2286
