from solver import build_matrix, rref, solve_coefficients
from fractions import Fraction

def test_build_matrix():
    assert build_matrix([('H2', {'H': 2}, 1), ('O2', {'O': 2}, 1), ('H2O', {'H': 2, 'O': 1}, -1)]) == [[2, 0, -2], [0, 2, -1]]


def test_rref():
    matrix = [[1, 2, -1, -4], [2, 3, -1, -11], [-2, 0, -3, 22]]
    assert rref(matrix) == [[1, 0, 0, -8], [0, 1, 0, 1], [0, 0, 1, -2]]


def test_solve_coefficients():
    matrix = [[Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(-1, 3)],
              [Fraction(0, 1), Fraction(1, 1), Fraction(0, 1), Fraction(-7, 6)],
              [Fraction(0, 1), Fraction(0, 1), Fraction(1, 1), Fraction(-2, 3)]]
    assert solve_coefficients(matrix) == [2, 7, 4, 6]