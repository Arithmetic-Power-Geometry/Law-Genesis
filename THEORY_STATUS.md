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

## Exact finite results represented in the repository

### Common-law congruence representation

A quotient supports one effective law for all microscopic laws exactly when its kernel is a congruence containing all raw microscopic disagreements. Therefore the finest valid quotient is the quotient by the least such congruence.

Status: mathematical theorem; implementation provided by `least_common_law_congruence`.

### Law Genesis Cost versus critical seed rank

The cycle-plus-constant family and identity-plus-constant family have the same maximal Law Genesis Cost `log2(n)`, but their critical seed ranks are respectively `1` and `n-1`.

Status: exact finite family; regression tests included.

### Exhaustive three- and four-state checks

All 378 unordered two-law families on a three-state carrier and all 32,896 unordered two-law families on a four-state carrier were enumerated.

For three states, every observed Law Genesis Cost value occurs with more than one critical seed rank.

For four states, the separation is stronger: systems with the same `Gamma` occur with `beta` values ranging across multiple levels. In particular, at `Gamma = 2` bits there are systems with `beta = 1`, `beta = 2`, and `beta = 3`.

Status: exhaustive finite computation; frozen machine-readable results in `results/exhaustive_n3_two_law.json` and `results/exhaustive_n4_two_law.json`.

### Nonlinear common-law depth witness

A three-law nonlinear construction has equal Law Genesis Cost at the first two observed depths and separates at the next depth. The witness is retained as a finite benchmark, not as an arbitrary-depth theorem.

Status: exact explicit finite witness; regression test and generated results included.

## Established machinery that is not claimed as new

- generated congruences and quotient algebras;
- invariant subspaces and linear reachability;
- matrix-word and transformation-semigroup behavior;
- Jordan/Weyr rank sequences;
- matroid dependence;
- noncommuting projection effects;
- Min-Sum Set Cover and related submodular scheduling reductions.

In particular, the linear form of the common-law closure reduces to a classical smallest invariant/reachable subspace construction. This is treated as a reduction theorem and novelty boundary, not as a new linear-algebraic mechanism.

## Current residual research target

The strongest unresolved direction is to determine whether nonlinear multi-law common-law closure has structural separation results that cannot be reduced to standard congruence, automata, semigroup, bisimulation, or control-theoretic invariants.

The project therefore treats computational searches primarily as falsification tools. A finite passing example is not interpreted as proof of novelty.

## Claim discipline

Results should be labeled as one of:

- **proved** — supported by a mathematical proof;
- **exhaustively verified** — all systems inside a stated finite search domain were enumerated;
- **computational witness** — a particular finite construction was verified;
- **conjecture/open** — not established;
- **reduction** — shown to coincide with established mathematics.
