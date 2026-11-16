from solver import build_matrix

def test_build_matrix():
    assert build_matrix([('H2', {'H': 2}, 1), ('O2', {'O': 2}, 1), ('H2O', {'H': 2, 'O': 1}, -1)]) == [[2, 0, -2], [0, 2, -1]]