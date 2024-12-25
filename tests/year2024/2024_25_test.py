from main import file_reader
from main.year2024.day_25 import solve_1

input = file_reader.read(file_name="day25.txt", path="tests/year2024/resources")


def test_solve_1():
    assert solve_1(input) == 3
