import pytest
from parsing import parse_species, split_sides, split_species, parse_equation

def test_parse_species():
    assert parse_species("H2O")[0] == {"H": 2, "O": 1}
    assert parse_species("NaCl")[0] == {"Na": 1, "Cl": 1}
    assert parse_species("CO")[0] == {"C": 1, "O": 1}
    assert parse_species("CH3COOH")[0] == {"C": 2, "H": 4, "O": 2}
    assert parse_species("Ca(OH)2")[0] == {"Ca": 1, "O": 2, "H": 2}
    assert parse_species("K4[Fe(CN)6]")[0] == {"K": 4, "Fe": 1, "C": 6, "N": 6}
    assert parse_species("C(CH3)3")[0] == {"C": 4, "H": 9}


def test_split_sides():
    assert split_sides("C2H6 + O2 -> CO2 + H2O") == ("C2H6 + O2", "CO2 + H2O")

def test_split_species():
    assert split_species("C2H6 + O2") == ["C2H6", "O2"]
    assert split_species("H2O") == ["H2O"]

def test_split_species_empty():
    for incorrect in ["H2 + + O2", "+ O2", "O2 +"]:
        with pytest.raises(ValueError):
            split_species(incorrect)

def test_parse_equation():
    assert parse_equation("H2 + O2 -> H2O") == [('H2', {'H': 2}, 1), ('O2', {'O': 2}, 1), ('H2O', {'H': 2, 'O': 1}, -1)]