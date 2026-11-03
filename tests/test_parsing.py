import pytest
from parsing import parse

def test_simple_formulas():
    assert parse("H2O")[0] == {"H": 2, "O": 1}
    assert parse("NaCl")[0] == {"Na": 1, "Cl": 1}
    assert parse("CO")[0] == {"C": 1, "O": 1}
    assert parse("CH3COOH")[0] == {"C": 2, "H": 4, "O": 2}

