from main import file_reader
from main.year2025.day_02 import solve_1, solve_2

input = file_reader.read(file_name="day02.txt", path="tests/year2025/resources")


def test_solve_1():
    assert solve_1(input) == 1227775554


def test_solve_2():
    assert solve_2(input) == 4174379265
