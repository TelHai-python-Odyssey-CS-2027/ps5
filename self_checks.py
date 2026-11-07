"""Student-facing self-checks for PS5 (same cases as the autograder).

Colab notebooks import this file and call the run_* helpers after your
functions are defined.
"""
from __future__ import annotations

import copy


def _same(got, expected, tol=None):
    if tol is None:
        return got == expected
    if isinstance(expected, (list, tuple)):
        return (
            isinstance(got, (list, tuple))
            and len(got) == len(expected)
            and all(_same(g, e, tol) for g, e in zip(got, expected))
        )
    try:
        return abs(got - expected) <= tol
    except TypeError:
        return False


def _run_groups(func, func_name, groups):
    earned = total = 0
    for title, points, cases in groups:
        problems = []
        for args, expected, tol, hint in cases:
            call = f"{func_name}({', '.join(repr(a) for a in args)})"
            try:
                got = func(*copy.deepcopy(args))
            except Exception as e:
                problems.append(
                    f"    Case failed: {call}\n    Raised {type(e).__name__}: {e}"
                )
                continue
            if not _same(got, expected, tol):
                msg = (
                    f"    Case failed: {call}\n"
                    f"    Expected: {expected!r}\n"
                    f"    Got:      {got!r}"
                )
                if hint:
                    msg += f"\n    Hint:     {hint}"
                problems.append(msg)
        total += points
        if problems:
            print(f"[FAIL] {title}  (0/{points} pt)")
            print("\n".join(problems))
        else:
            earned += points
            print(f"[PASS] {title}  ({points}/{points} pt)")
    print(f"\nSelf-check score: {earned}/{total}")
    return earned == total


COUNT_ATOMS_GROUPS = [
    (
        "count_atoms_in_molecule: simple (H2O / H2C)",
        1,
        [
            (("H2O",), {"H": 2, "O": 1}, None, "'H2O' -> two H and one O"),
            (("H2C",), {"H": 2, "C": 1}, None, "same idea with C instead of O"),
        ],
    ),
    (
        "count_atoms_in_molecule: multi-letter symbols",
        1,
        [
            (("He",), {"He": 1}, None, "two-letter symbol with no digit -> count 1"),
            (("F4He2",), {"F": 4, "He": 2}, None, "split on capitals, then read digits"),
        ],
    ),
    (
        "count_atoms_in_molecule: no digit",
        1,
        [
            (("Ir",), {"Ir": 1}, None, "no digit means count 1"),
            (("NaCl",), {"Na": 1, "Cl": 1}, None, "each piece without a digit counts as 1"),
        ],
    ),
    (
        "count_atoms_in_molecule: sugar C6H12O6",
        1,
        [
            (("C6H12O6",), {"C": 6, "H": 12, "O": 6}, None, "read the full number after each symbol"),
        ],
    ),
    (
        "count_atoms_in_molecule: repeated element",
        1,
        [
            (("H2OH",), {"H": 3, "O": 1}, None, "same key can appear twice — add the counts"),
        ],
    ),
]


BALANCE_GROUPS = [
    (
        "balance_reaction: H2 + O2 -> H2O",
        1,
        [
            (("H2 + O2 -> H2O",), [1.0, 0.5, 1], 1e-9, "last product coefficient is fixed to 1"),
        ],
    ),
    (
        "balance_reaction: N2 + H2 -> NH3",
        1,
        [
            (("N2 + H2 -> NH3",), [0.5, 1.5, 1], 1e-9, "2 NH3 needs 1 N2 and 3 H2 → half-integers with last=1"),
        ],
    ),
    (
        "balance_reaction: CH4 + O2 -> CO2 + H2O",
        1,
        [
            (("CH4 + O2 -> CO2 + H2O",), [0.5, 1.0, 0.5, 1], 1e-9, "methane combustion with last coeff 1"),
        ],
    ),
    (
        "balance_reaction: Fe2O3 + H2 -> Fe + H2O",
        1,
        [
            (("Fe2O3 + H2 -> Fe + H2O",), [1 / 3, 1.0, 2 / 3, 1], 1e-9, "iron oxide reduction; floats like 1/3 are OK"),
        ],
    ),
    (
        "balance_reaction: C3H8 + O2 -> CO2 + H2O",
        1,
        [
            (("C3H8 + O2 -> CO2 + H2O",), [0.25, 1.25, 0.75, 1], 1e-9, "propane; check O balance carefully"),
        ],
    ),
]


def run_count_atoms_checks(func):
    """Run count_atoms_in_molecule self-checks. Pass the function object."""
    return _run_groups(func, "count_atoms_in_molecule", COUNT_ATOMS_GROUPS)


def run_balance_checks(func):
    """Run balance_reaction self-checks. Pass the function object."""
    return _run_groups(func, "balance_reaction", BALANCE_GROUPS)
