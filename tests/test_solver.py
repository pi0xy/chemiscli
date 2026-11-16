from solver import build_matrix, rref

def test_build_matrix():
    assert build_matrix([('H2', {'H': 2}, 1), ('O2', {'O': 2}, 1), ('H2O', {'H': 2, 'O': 1}, -1)]) == [[2, 0, -2], [0, 2, -1]]


def test_rref():
    matrix = [[1, 2, -1, -4], [2, 3, -1, -11], [-2, 0, -3, 22]]
    assert rref(matrix) == [[1, 0, 0, -8], [0, 1, 0, 1], [0, 0, 1, -2]]