# PS5 — Balancing chemical reactions

Wire together string parsing, dictionaries, imports, and SymPy to balance a reaction.

**Due (Odyssey):** 18/11/2026 at 08:00 (Asia/Jerusalem).

## What to change

### 1. `string_utils.py`

Implement (you may reuse PS4):

- `split_before_each_uppercases(formula)`
- `split_at_first_digit(formula)`

Then fill the three missing lines in `count_atoms_in_molecule` (init dict, update counts, return).

```python
count_atoms_in_molecule("H2O")  # {'H': 2, 'O': 1}
```

Keep `parse_chemical_reaction` and `count_atoms_in_reaction` as given.

### 2. `equation_utils.py`

Add the SymPy imports at the top. `my_solve` calls `sympy_solve` — import `solve` under that name, and also import `symbols` and `Eq`.

### 3. `main.py`

Import every name `balance_reaction` uses from `string_utils` and `equation_utils`.

## Practice in Colab (optional)

**From GitHub:** use **Ctrl+click** / **⌘+click** (or middle-click) so Colab opens in a new tab.

- `count_atoms_in_molecule`:
  <a href="https://colab.research.google.com/github/TelHai-python-Odyssey-CS-2027/ps5/blob/main/count_atoms_in_molecule.ipynb" target="_blank" rel="noopener noreferrer"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
- Full pipeline (`balance_reaction`):
  <a href="https://colab.research.google.com/github/TelHai-python-Odyssey-CS-2027/ps5/blob/main/main.ipynb" target="_blank" rel="noopener noreferrer"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Notebooks are not graded — only the `.py` files count. Each notebook loads `self_checks.py` and runs the **same cases** as the autograder (expected / got / hint).

## Submit

1. Accept the Classroom 50 assignment.
2. Edit the three `.py` files above, then **Commit changes**.
3. Check the latest autograding run for your score.

## Grading — 10 points

| Check | Points |
| --- | ---: |
| `count_atoms_in_molecule` — simple (`H2O`, `H2C`) | 1 |
| `count_atoms_in_molecule` — multi-letter (`He`, `F4He2`) | 1 |
| `count_atoms_in_molecule` — no digit (`Ir`, `NaCl`) | 1 |
| `count_atoms_in_molecule` — sugar (`C6H12O6`) | 1 |
| `count_atoms_in_molecule` — repeated element (`H2OH`) | 1 |
| `balance_reaction` — `H2 + O2 -> H2O` | 1 |
| `balance_reaction` — `N2 + H2 -> NH3` | 1 |
| `balance_reaction` — `CH4 + O2 -> CO2 + H2O` | 1 |
| `balance_reaction` — `Fe2O3 + H2 -> Fe + H2O` | 1 |
| `balance_reaction` — `C3H8 + O2 -> CO2 + H2O` | 1 |

## Optional: keep Colab work in Drive

In Colab: **File → Save a copy in Drive**.
