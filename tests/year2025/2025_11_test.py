from main import file_reader
from main.year2025.day_11 import solve_1, solve_2


def test_solve_1():
    input = file_reader.read(file_name="day11_1.txt", path="tests/year2025/resources")
    assert solve_1(input) == 5


def test_solve_2():
    input = file_reader.read(file_name="day11_2.txt", path="tests/year2025/resources")
    assert solve_2(input) == 2
