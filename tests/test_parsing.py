import pytest
from parsing import parse_species

def test_parse_species():
    assert parse_species("H2O")[0] == {"H": 2, "O": 1}
    assert parse_species("NaCl")[0] == {"Na": 1, "Cl": 1}
    assert parse_species("CO")[0] == {"C": 1, "O": 1}
    assert parse_species("CH3COOH")[0] == {"C": 2, "H": 4, "O": 2}

