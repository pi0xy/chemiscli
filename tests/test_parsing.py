import pytest
from parsing import parse_species

def test_parse_species():
    assert parse_species("H2O")[0] == {"H": 2, "O": 1}
    assert parse_species("NaCl")[0] == {"Na": 1, "Cl": 1}
    assert parse_species("CO")[0] == {"C": 1, "O": 1}
    assert parse_species("CH3COOH")[0] == {"C": 2, "H": 4, "O": 2}
    assert parse_species("Ca(OH)2")[0] == {"Ca": 1, "O": 2, "H": 2}
    assert parse_species("K4[Fe(CN)6]")[0] == {"K": 4, "Fe": 1, "C": 6, "N": 6}
    assert parse_species("C(CH3)3")[0] == {"C": 4, "H": 9}