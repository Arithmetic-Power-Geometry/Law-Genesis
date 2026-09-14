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

### Law Genesis Cost versus critical seed rank

The cycle-plus-constant family and identity-plus-constant family have the same maximal Law Genesis Cost `log2(n)`, but their critical seed ranks are respectively `1` and `n-1`.

Status: exact finite family; regression tests included.

### Exhaustive three- and four-state checks

All 378 unordered two-law families on a three-state carrier and all 32,896 unordered two-law families on a four-state carrier were enumerated.

For three states, every observed Law Genesis Cost value occurs with more than one critical seed rank.

For four states, the separation is stronger: systems with the same `Gamma` occur with `beta` values ranging across multiple levels. In particular, at `Gamma = 2` bits there are systems with `beta = 1`, `beta = 2`, and `beta = 3`.

Status: exhaustive finite computation; frozen machine-readable results in `results/exhaustive_n3_two_law.json` and `results/exhaustive_n4_two_law.json`.

### Strong nonlinear common-law depth witness

The five-state three-law witness uses the same intervention in both systems. At depths 0 and 1 the two systems agree on all of the following recorded observables:

- Law Genesis Cost `Gamma`;
- common-law congruence class-size profile;
- raw disagreement-pair count;
- critical seed rank `beta`;
- the complete one-seed fragility spectrum.

At depth 2 they still have the same raw disagreement-pair count (`1`) and the same critical seed rank (`2`), yet the common-law closures differ:

- System A has class sizes `(3,1,1)` and `Gamma = (3/5) log2(3) ≈ 0.95098` bits;
- System B has class sizes `(2,1,1,1)` and `Gamma = 0.4` bits.

Thus the matched low-depth summaries do not determine the next common-law closure geometry for this explicit nonlinear multi-law pair.

Status: exact explicit finite witness; strengthened regression tests and generated diagnostics included.

### Arbitrary-delay Law-Genesis separation theorem

For every prescribed finite depth `D >= 2`, the five-state nonlinear witness can be lifted to two finite three-law systems on a common carrier with one common intervention such that, at every depth `t < D`, the systems have equal `Gamma`, equal common-law class-size profiles, and equal raw disagreement counts, while at depth `D` their Law Genesis Costs differ.

The construction uses a shared delay-line carrier `X x {0,...,d}` with `d = D-2`. Lifted microscopic laws write their outputs into the top layer. The common intervention shifts the active layer downward and applies the original nonlinear intervention only after layer 0 is reached. Before the final two stages the closure is isomorphic to the base depth-0 closure; the next stage is the base depth-1 closure; and the separating stage is the base depth-2 closure.

For `d+1` layers, the separating costs are

- `Gamma_A = ((3/5) log2(3))/(d+1)`;
- `Gamma_B = 0.4/(d+1)`.

The gap is nonzero for every finite `d`.

Status: exact constructive theorem. The proof is recorded in `THEOREMS.md`; regression tests cover several delays; generated CSV/JSON results are produced by the reproduction script.

Novelty boundary: the delay-line mechanism itself is not claimed as a new automata, semigroup, or control mechanism. The theorem establishes unbounded Law-Genesis depth for the framework, but the next flagship target is an intrinsic nonlinear family whose growing depth does not come from an explicit delay gadget.

### Exhaustive three-state multi-law depth kill test

The repository exhaustively tested all unordered three-law families on three states against every three-state intervention. The search required two candidate systems to use the same intervention and to agree at depths 0 and 1 on `Gamma`, class-size profile, raw disagreement count, `beta`, and the complete one-seed fragility spectrum; it also required equal raw disagreement count at depth 2 while seeking a different depth-2 `Gamma`.

No witness exists inside this complete three-state search domain under those constraints.

Status: exhaustively verified negative result for the stated finite domain. This does not rule out four-state or larger witnesses and is not a general impossibility theorem.

## Established machinery that is not claimed as new

- generated congruences and quotient algebras;
- invariant subspaces and linear reachability;
- matrix-word and transformation-semigroup behavior;
- Jordan/Weyr rank sequences;
- matroid dependence;
- noncommuting projection effects;
- Min-Sum Set Cover and related submodular scheduling reductions;
- generic delay-line constructions used to postpone observable effects.

In particular, the linear form of the common-law closure reduces to a classical smallest invariant/reachable subspace construction. This is treated as a reduction theorem and novelty boundary, not as a new linear-algebraic mechanism.

## Current residual research target

The arbitrary-depth existence question is now solved constructively, but only by an explicit delay lift. The strongest unresolved direction is therefore stricter:

> Find an intrinsic nonlinear multi-law family whose Law-Genesis depth grows with system size because of common-law closure geometry itself, while preserving matched low-order observables, and then test whether that statement reduces to standard congruence, automata, semigroup, bisimulation, or control-theoretic invariants.

The project treats computational searches primarily as falsification tools. A finite passing example or an artificial delay construction is not interpreted as proof of mathematical novelty.

## Claim discipline

Results should be labeled as one of:

- **proved** — supported by a mathematical proof;
- **exhaustively verified** — all systems inside a stated finite search domain were enumerated;
- **computational witness** — a particular finite construction was verified;
- **conjecture/open** — not established;
- **reduction** — shown to coincide with established mathematics.
