from main import file_reader
from main.day_10 import solve_1, solve_2

input = file_reader.read(file_name="day10.txt", path="tests/resources")


def test_solve_1():
    input = [
        "..F7.",
        ".FJ|.",
        "SJ.L7",
        "|F--J",
        "LJ...",
    ]
    assert solve_1(input) == 8


def test_solve_2():
    assert solve_2(input) == 10
