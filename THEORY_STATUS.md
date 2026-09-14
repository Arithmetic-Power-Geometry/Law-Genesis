# Theory Status

This file records the present mathematical status of the Law Genesis project. It separates exact results from reductions to established mathematics and from open research targets.

## Frozen core

For a finite state space `X` and microscopic law family `F = {f1, ..., fm}`:

1. `R_F` is the set of pointwise output disagreements among microscopic laws.
2. `Theta_F` is the least congruence containing `R_F` and compatible with every law in `F`.
3. `X / Theta_F` is the finest quotient on which all microscopic laws induce one effective law.
4. For a uniform finite state space, `Gamma(F) = H(X | X/Theta_F)` is the Law Genesis Cost.
5. Forced Abstraction measures the extra loss created by congruence closure beyond a deliberately imposed seed identification.
6. `beta(F)` is the minimum number of seed pairs whose compatible closure is universal.
7. Protocol-conditioned `Gamma(w)` evaluates Law Genesis Cost after an intervention word.
8. Genesis Work sums protocol-conditioned Law Genesis Cost over successive prefixes.

## Exact results represented in the repository

### Common-law congruence representation

A quotient supports one effective law for all microscopic laws exactly when its kernel is a congruence containing all raw microscopic disagreements. Therefore the finest valid quotient is the quotient by the least such congruence.

Status: mathematical theorem; implementation provided by `least_common_law_congruence`.

### Fixed raw-disagreement separation

The five-state nonlinear construction yields two three-law systems whose raw disagreement relations are not merely equal in cardinality but are exactly identical at the separating stage:

`R_A = R_B = {(0,2)}`.

Nevertheless their least common-law congruences differ:

- System A: `{{0,1,2},{3},{4}}`, giving `Gamma = (3/5) log2(3)`;
- System B: `{{0,2},{1},{3},{4}}`, giving `Gamma = 0.4` bits.

A direct proof is recorded in `THEOREMS.md`: in A, compatibility of the seed pair `0~2` under one transformed law forces `1~0`, whereas in B every transformed law maps the pair `{0,2}` back into itself, so no third state is forced into the class.

Stronger still, under the shared intervention the two systems have exactly the same raw disagreement relation at every observed depth 0, 1, and 2, while their common-law congruences first diverge at depth 2.

Status: exact finite structural theorem with direct proof and regression test.

Interpretation: the amount and identity of raw microscopic disagreement do not determine the information cost of making that disagreement dynamically consistent. The closure geometry matters.

### Law Genesis Cost versus critical seed rank

The cycle-plus-constant family and identity-plus-constant family have the same maximal Law Genesis Cost `log2(n)`, but their critical seed ranks are respectively `1` and `n-1`.

Status: exact finite family; regression tests included.

### Exhaustive three- and four-state checks

All 378 unordered two-law families on a three-state carrier and all 32,896 unordered two-law families on a four-state carrier were enumerated.

For three states, every observed Law Genesis Cost value occurs with more than one critical seed rank.

For four states, the separation is stronger: systems with the same `Gamma` occur with `beta` values ranging across multiple levels. In particular, at `Gamma = 2` bits there are systems with `beta = 1`, `beta = 2`, and `beta = 3`.

Status: exhaustive finite computation; frozen machine-readable results in `results/exhaustive_n3_two_law.json` and `results/exhaustive_n4_two_law.json`.

### Strong nonlinear common-law depth witness

The five-state three-law witness uses the same intervention in both systems. At depths 0 and 1 the two systems agree on Law Genesis Cost, common-law class-size profile, exact raw disagreement relation, critical seed rank, and the complete one-seed fragility spectrum.

At depth 2 they still have the same exact raw disagreement relation `R={(0,2)}` and the same critical seed rank `beta=2`, yet the common-law closures and Law Genesis Costs differ.

Status: exact explicit finite witness; strengthened regression tests and generated diagnostics included.

### Arbitrary-delay Law-Genesis separation theorem

For every prescribed finite depth `D >= 2`, the five-state nonlinear witness can be lifted to two finite three-law systems on a common carrier with one common intervention such that, at every depth `t < D`, the systems have equal `Gamma`, equal common-law class-size profiles, and equal raw disagreement counts, while at depth `D` their Law Genesis Costs differ.

Status: exact constructive theorem. The proof is recorded in `THEOREMS.md`; regression tests cover several delays; generated CSV/JSON results are produced by the reproduction script.

Novelty boundary: the delay-line mechanism itself is not claimed as a new automata, semigroup, or control mechanism. It establishes unbounded Law-Genesis depth inside the framework but is not the flagship novelty claim.

### Exhaustive three-state multi-law depth kill test

The repository exhaustively tested all unordered three-law families on three states against every three-state intervention under strong matching constraints. No depth-2 separating witness exists inside that complete domain.

Status: exhaustively verified negative result for the stated finite domain. This is not a general impossibility theorem.

## Established machinery that is not claimed as new

- generated congruences and quotient algebras;
- invariant subspaces and linear reachability;
- matrix-word and transformation-semigroup behavior;
- Jordan/Weyr rank sequences;
- matroid dependence;
- noncommuting projection effects;
- Min-Sum Set Cover and related submodular scheduling reductions;
- generic delay-line constructions used to postpone observable effects.

In particular, the linear form of the common-law closure reduces to a classical smallest invariant/reachable subspace construction. Repeated application of a single deterministic intervention also lies inside ordinary finite transformation-semigroup dynamics. These are treated as reduction boundaries, not new mechanisms.

## Current residual research target

The strongest current structural result is now the fixed raw-disagreement separation, because it isolates the specific Law-Genesis phenomenon without relying on a delay gadget: identical raw disagreement can generate different dynamically forced abstractions.

The next target is therefore not merely a longer protocol depth. It is to strengthen the fixed-disagreement theorem by matching progressively richer pre-closure invariants while still forcing different least common-law congruences. Candidate invariants include the exact raw disagreement graph, per-state output multiplicities, degree sequence, orbit summaries, and low-order closure statistics.

A scalable family of such separations would be stronger than an arbitrary-depth result produced only by semigroup timing.

The project treats computational searches primarily as falsification tools. A finite witness, passing software test, or artificial delay construction is not interpreted as proof of novelty against neighboring literatures.

## Claim discipline

Results should be labeled as one of:

- **proved** — supported by a mathematical proof;
- **exhaustively verified** — all systems inside a stated finite search domain were enumerated;
- **computational witness** — a particular finite construction was verified;
- **conjecture/open** — not established;
- **reduction** — shown to coincide with established mathematics.
