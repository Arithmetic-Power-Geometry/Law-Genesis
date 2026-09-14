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

The five-state nonlinear construction yields two three-law systems whose raw disagreement relations are exactly identical at the separating stage:

`R_A = R_B = {(0,2)}`.

Nevertheless their least common-law congruences differ:

- System A: `{{0,1,2},{3},{4}}`, giving `Gamma = (3/5) log2(3)`;
- System B: `{{0,2},{1},{3},{4}}`, giving `Gamma = 0.4` bits.

A direct proof is recorded in `THEOREMS.md`. Stronger still, under the shared intervention the two systems have exactly the same raw disagreement relation at observed depths 0, 1, and 2, while their common-law congruences first diverge at depth 2.

Status: exact finite structural theorem with direct proof and regression test.

Interpretation: the amount and identity of raw microscopic disagreement do not determine the information cost of making that disagreement dynamically consistent. The closure geometry matters.

### Law Genesis Cost versus critical seed rank

The cycle-plus-constant family and identity-plus-constant family have the same maximal Law Genesis Cost `log2(n)`, but their critical seed ranks are respectively `1` and `n-1`.

Status: exact finite family; regression tests included.

### Exhaustive three- and four-state checks

All 378 unordered two-law families on a three-state carrier and all 32,896 unordered two-law families on a four-state carrier were enumerated.

For three states, every observed Law Genesis Cost value occurs with more than one critical seed rank. For four states, at `Gamma = 2` bits there are systems with `beta = 1`, `beta = 2`, and `beta = 3`.

Status: exhaustive finite computation; frozen machine-readable results in `results/exhaustive_n3_two_law.json` and `results/exhaustive_n4_two_law.json`.

### Strong nonlinear common-law depth witness

The five-state three-law witness uses the same intervention in both systems. At depths 0 and 1 the two systems agree on Law Genesis Cost, common-law class-size profile, exact raw disagreement relation, critical seed rank, and the complete one-seed fragility spectrum.

At depth 2 they still have the same exact raw disagreement relation `R={(0,2)}` and the same critical seed rank `beta=2`, yet the common-law closures and Law Genesis Costs differ.

Status: exact explicit finite witness; strengthened regression tests and generated diagnostics included.

### Clock-free four-state permutation witness

A four-state, three-law pair under the common permutation intervention `P=(1,2,3,0)` matches through depths 0, 1, and 2 on `Gamma`, common-law class-size profile, raw disagreement count, critical seed rank, and complete one-seed fragility spectrum, but separates at depth 3:

- System A: `Gamma(3)=2` bits;
- System B: `Gamma(3)=1.188721875541` bits.

The intervention is a permutation, so the construction contains no transient countdown layers.

Status: deterministic computational witness, frozen in source and regression tests. It is not an arbitrary-depth theorem.

### Strong-invariant four-state kill test

A stronger deterministic search tested 96,000 sampled three-law systems across all 24 four-state permutation interventions. Candidate pairs were required to match through depths 0, 1, and 2 on:

- `Gamma`;
- common-law class-size profile;
- raw disagreement graph isomorphism type;
- sorted per-state microscopic-output multiplicities;
- critical seed rank `beta`;
- complete one-seed fragility spectrum.

The search examined 94,180 cheap-signature collisions and 208,367 strong-signature comparisons and found no pair whose `Gamma` separated at depth 3.

Status: deterministic negative computational result for the stated sample budget and search domain. It is not an impossibility theorem. Frozen output: `results/intrinsic_strong_search.json`.

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

The v1.0 flagship foundations result set is now frozen sufficiently for manuscript drafting. The strongest structural theorem remains the fixed raw-disagreement separation: identical raw disagreement can generate different dynamically forced abstractions and different information costs.

The four-state intrinsic permutation witness demonstrates later divergence without an explicit delay gadget. The stronger 96,000-system search did not find a depth-3 witness after additionally matching richer pre-closure invariants; this should be reported as a bounded negative computational result, not as evidence of impossibility.

Open problems include:

- arbitrary-depth intrinsic nonlinear separation without a delay gadget;
- scalable fixed-disagreement families with richer matched pre-closure invariants;
- sharper complexity bounds for common-law congruence computation and fragility quantities;
- approximate Law Genesis Cost `Gamma_epsilon`.

These are now post-v1.0 research directions rather than prerequisites for the first foundations paper.

## Claim discipline

Results should be labeled as one of:

- **proved** — supported by a mathematical proof;
- **exhaustively verified** — all systems inside a stated finite search domain were enumerated;
- **computational witness** — a particular finite construction was verified;
- **deterministic negative search** — no witness was found inside a precisely stated sampled search domain;
- **conjecture/open** — not established;
- **reduction** — shown to coincide with established mathematics.
