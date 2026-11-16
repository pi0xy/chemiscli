# CHEMISCLI

**Chemiscli** est un équilibreur d'équations chimiques sous forme de CLI.

La méthode de résolution utilisée est la conversion de l'équation en système d'équations linéaires, mis sous forme matricielle et résolu par la méthode de Gauss-Jordan.

## Installation et utilisation

Prérequis : Python 3.9+ (pour `math.lcm`)

```
python main.py
```

Exemple:

```
Equation: C2H6 + O2 -> CO2 + H2O
2 C2H6 + 7 O2 -> 4 CO2 + 6 H2O
```

Format: "->" entre réactifs et produits, "+" entre les espèces, parenthèses et crochets acceptés

## Méthode

L'équation est convertie en matrice (lignes = éléments, colonnes = espèces). La matrice est ensuite réduite par la méthode de Gauss-Jordan, puis les coefficients sont extraits du noyau et ramenés aux plus petits entiers grâce au PPCM de leurs dénominateurs.


## Tests

```
python -m pytest
```


## Sources

- https://rosettacode.org/wiki/Reduced_row_echelon_form
- https://fr.wikipedia.org/wiki/%C3%89limination_de_Gauss-Jordan