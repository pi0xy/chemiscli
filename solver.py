from fractions import Fraction
from math import gcd, lcm

def build_matrix(species_list):

    elements = []
    for name, atoms, sign in species_list:
        for element in atoms:
            if element not in elements:
                elements.append(element)

    matrix = []

    for element in elements:
        row = []
        for name, atoms, sign in species_list:
            value = sign * atoms.get(element, 0)
            row.append(value)
        matrix.append(row)

    return matrix


def rref(matrix):
    matrix = [[Fraction(value) for value in row] for row in matrix]
    column = 0
    row_count = len(matrix)
    column_count = len(matrix[0])
    for row in range(row_count):
        if column_count <= column:
            return matrix
        i = row
        while matrix[i][column] == 0:
            i += 1
            if row_count == i:
                i = row
                column += 1
                if column_count == column:
                    return matrix
        matrix[i], matrix[row] = matrix[row], matrix[i]
        if matrix[row][column] != 0:
            pivot = matrix[row][column]
            for k in range(column_count):
                matrix[row][k] /= pivot

        for other in range(row_count):
            if other != row:
                factor = matrix[other][column]
                for k in range(column_count):
                    matrix[other][k] -= factor * matrix[row][k]
        column += 1
    return matrix


def solve_coefficients(matrix):
    column_count = len(matrix[0])

    free = column_count - 1

    x = []
    for r in range(free):
        x.append(-matrix[r][free])
    x.append(Fraction(1))

    multiple = 1
    for value in x:
        multiple = lcm(multiple, value.denominator)

    coefficients = []
    for value in x:
        coefficients.append(int(value*multiple))
    return coefficients


matrix = [[2, 0, -1,  0],
          [6, 0,  0, -2],
          [0, 2, -2, -1]]

print(rref(matrix))