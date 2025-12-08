from main.year2017.day_11 import solve_1, solve_2


def test_solve_1():
    assert solve_1("ne,ne,ne") == 3
    assert solve_1("ne,ne,sw,sw") == 0
    assert solve_1("ne,ne,s,s") == 2
    assert solve_1("se,sw,se,sw,sw") == 3


def test_solve_2():
    assert solve_2("ne,ne,ne") == 3
    assert solve_2("ne,ne,sw,sw") == 2
    assert solve_2("ne,ne,s,s") == 2
    assert solve_2("se,sw,se,sw,sw") == 3
