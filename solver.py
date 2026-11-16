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