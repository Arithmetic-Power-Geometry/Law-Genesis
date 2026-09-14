# Final Theory Freeze Checklist

This checklist defines the last synchronization pass before the flagship Law Genesis manuscript is drafted.

## 1. Strong intrinsic search

- `scripts/search_intrinsic_strong.py` completed with the frozen deterministic seed and search budget.
- Exact output is preserved in `results/intrinsic_strong_search.json`.
- Result: no witness was found among 96,000 sampled three-law systems across all 24 four-state permutation interventions under the stronger matched-invariant constraints.
- This is recorded only as a deterministic negative sampled search, not as an impossibility theorem.

Status: complete.

## 2. Headline theorem ledger

The manuscript may use the following statements only with their stated status:

- Common-Law Congruence Representation — proved representation theorem using standard generated-congruence machinery.
- Fixed Raw-Disagreement Separation — proved explicit finite theorem.
- Law Genesis Cost versus critical seed rank — proved explicit family.
- Exhaustive two-law three- and four-state separations — exhaustively verified finite computation.
- Five-state nonlinear common-law depth witness — exact explicit finite witness.
- Four-state permutation depth witness — deterministic clock-free computational witness.
- Strong-invariant four-state search — deterministic negative sampled search; no depth-3 witness found in the stated domain.
- Arbitrary-Delay Law-Genesis Separation — proved constructive theorem, with explicit delay-line novelty boundary.
- Arbitrary-depth intrinsic nonlinear separation — open.

Status: complete for v1.0.

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

Status: complete for the current claim set; see `PRIOR_ART_KILL_PASS.md`.

## 4. Reproducibility freeze

The checked final-freeze workflow completed successfully for:

- `pytest -q`;
- `python scripts/reproduce.py`;
- `python scripts/search_multilaw_depth.py`;
- `python scripts/search_intrinsic_depth.py`;
- `python scripts/search_intrinsic_strong.py`.

All headline results are now represented in committed source, theorem/status files, or committed machine-readable result files. `THEORY_STATUS.md`, `PAPER_READINESS.md`, and this checklist have been synchronized to the strong-search outcome.

Status: complete for v1.0.

## 5. Manuscript trigger

Sections 1–4 are complete.

Status: MANUSCRIPT DRAFTING SHOULD START NOW.

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

The manuscript should mark every claim as proved, exhaustively verified, deterministic computational witness, deterministic negative sampled search, reduction, or open.
