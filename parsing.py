def parse(formula, i=0):
    atoms_dict = {}
    while i < len(formula):
        if formula[i].isupper():
            current_element = formula[i]
            i += 1
            while i < len(formula) and formula[i].islower():
                current_element += formula[i]
                i += 1
            if i < len(formula) and formula[i].isdigit():
                current_coeff = formula[i]
                i += 1
                while i < len(formula) and formula[i].isdigit():
                    current_coeff += formula[i]
                    i += 1
            else:
                current_coeff = 1

            if atoms_dict.get(current_element, 0) == 0:
                atoms_dict[current_element] = int(current_coeff)
            else:
                atoms_dict[current_element] += int(current_coeff)
        else:
            pass

    return atoms_dict, i