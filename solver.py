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
