from parsing import parse_equation
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


def balance(equation):
    species_list = parse_equation(equation)
    coefficients = solve_coefficients(rref(build_matrix(species_list)))

    reactants = []
    products = []

    for i in range(len(species_list)):
        name = species_list[i][0]
        sign = species_list[i][2]
        coefficient = coefficients[i]

        if coefficient == 1:
            current_species = name
        else:
            current_species = str(coefficient) + " " + name


        if sign == 1:
            reactants.append(current_species)
        else:
            products.append(current_species)

    return " + ".join(reactants) + " -> " + " + ".join(products)