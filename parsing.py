def parse_species(species, i=0):
    atoms_dict = {}
    while i < len(species):
        if species[i].isupper():
            current_element = species[i]
            i += 1
            while i < len(species) and species[i].islower():
                current_element += species[i]
                i += 1
            if i < len(species) and species[i].isdigit():
                current_coeff = species[i]
                i += 1
                while i < len(species) and species[i].isdigit():
                    current_coeff += species[i]
                    i += 1
            else:
                current_coeff = 1

            if atoms_dict.get(current_element, 0) == 0:
                atoms_dict[current_element] = int(current_coeff)
            else:
                atoms_dict[current_element] += int(current_coeff)

        elif species[i] == "(" or species[i] == "[":
            sub_dict, i = parse_species(species, i+1)
            if i >= len(species):
                raise ValueError("unclosed parenthesis")
            i += 1
            if i < len(species) and species[i].isdigit():
                current_coeff = species[i]
                i += 1
                while i < len(species) and species[i].isdigit():
                    current_coeff += species[i]
                    i += 1
            else:
                current_coeff = 1

            for element, coeff in sub_dict.items():
                if atoms_dict.get(element, 0) == 0:
                    atoms_dict[element] = coeff * int(current_coeff)
                else:
                    atoms_dict[element] += coeff * int(current_coeff)

        elif species[i] == ")" or species[i] == "]":
            break

        else:
            raise ValueError("unknown character")

    return atoms_dict, i