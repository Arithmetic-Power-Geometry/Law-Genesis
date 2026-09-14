# Final Theory Freeze Checklist

This checklist defines the last synchronization pass before the flagship Law Genesis manuscript is drafted.

## 1. Strong intrinsic search

- Run `scripts/search_intrinsic_strong.py` with the frozen deterministic seed and search budget.
- Preserve the exact output in `results/intrinsic_strong_search.json`.
- If a witness is found, promote it to an explicit example module and regression test.
- If no witness is found, record the exact negative search domain and do not generalize it into an impossibility theorem.

Status: pending completion of the current optimized CI run.

## 2. Headline theorem ledger

The manuscript may use the following statements only with their stated status:

- Common-Law Congruence Representation — proved representation theorem using standard generated-congruence machinery.
- Fixed Raw-Disagreement Separation — proved explicit finite theorem.
- Law Genesis Cost versus critical seed rank — proved explicit family.
- Exhaustive two-law three- and four-state separations — exhaustively verified finite computation.
- Five-state nonlinear common-law depth witness — exact explicit finite witness.
- Four-state permutation depth witness — deterministic clock-free computational witness.
- Arbitrary-Delay Law-Genesis Separation — proved constructive theorem, with explicit delay-line novelty boundary.
- Arbitrary-depth intrinsic nonlinear separation — open.

## 3. Novelty boundary

The paper must not claim novelty for:

- generated congruences or quotient algebras;
- finite-state partition refinement;
- bisimulation and quotient transition systems;
- synchronizing automata or transformation semigroups;
- invariant/reachable subspaces in linear systems;
- Jordan/Weyr rank sequences;
- matroid dependence;
- delay-line constructions;
- Min-Sum Set Cover/submodular scheduling reductions.

The central framework claim should instead be framed around the structured coupling

`raw microscopic law disagreement -> least law-compatible closure -> information cost -> forced abstraction -> fragility -> sequential separation`.

## 4. Reproducibility freeze

Before manuscript drafting:

- `pytest -q` must pass;
- `python scripts/reproduce.py` must pass;
- `python scripts/search_multilaw_depth.py` must pass;
- `python scripts/search_intrinsic_depth.py` must pass;
- `python scripts/search_intrinsic_strong.py` must complete;
- all headline results must be represented in committed source or result files;
- `THEOREMS.md`, `THEORY_STATUS.md`, `PAPER_READINESS.md`, and result files must agree.

## 5. Manuscript trigger

Once Sections 1–4 are complete, stop broad theory invention and begin the flagship foundations paper.

Recommended narrative:

1. motivation: when can heterogeneous microscopic laws be represented by one reusable effective law?
2. common-law quotient constraint;
3. least compatible congruence and Law Genesis Cost;
4. forced abstraction and fragility;
5. exact structural separations;
6. nonlinear sequential/intrinsic witnesses;
7. exact reductions and novelty boundaries;
8. computational falsification and reproducibility;
9. open problems, especially arbitrary-depth intrinsic separation.

The manuscript should mark every claim as proved, exhaustively verified, deterministic computational witness, reduction, or open.
