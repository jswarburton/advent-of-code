from main import file_reader
from main.year2024.day_23 import solve_1, solve_2

input = file_reader.read(file_name="day23.txt", path="tests/year2024/resources")


def test_solve_1():
    assert solve_1(input) == 7


def test_solve_2():
    assert solve_2(input) == "co,de,ka,ta"
