# Law Genesis Theorems

This file records theorem statements that are supported either by direct proof or by an explicit finite verification. Standard machinery is identified separately from framework-specific interpretation.

## Common-Law Congruence Representation

Let `F = {f1, ..., fm}` be deterministic maps on a finite set `X`. Let `R_F` contain every pair `(fi(x), fj(x))`. A quotient `q : X -> Y` supports a single map `G : Y -> Y` satisfying `q fi = G q` for every `i` if and only if `ker(q)` is a congruence for all maps in `F` and contains `R_F`. Therefore the finest valid common-law quotient is `X / Theta_F`, where `Theta_F` is the least such congruence.

This is an application of standard generated-congruence machinery to the common-law constraint.

## Arbitrary-Delay Law-Genesis Separation

### Statement

For every integer `D >= 2`, there exist two finite three-law systems `A_D` and `B_D` on the same carrier and with the same single intervention `T_D` such that, for every depth `t < D`,

- their Law Genesis Costs are equal;
- their least-common-law congruences have the same class-size profile; and
- their raw disagreement-pair counts are equal;

but at depth `D`,

`Gamma_A_D(T_D^D) != Gamma_B_D(T_D^D)`.

Hence Law-Genesis separation can occur at arbitrarily large finite protocol depth.

### Construction

Start from the verified five-state nonlinear three-law witness `(A, B, N)` whose systems match at base depths 0 and 1 and separate at base depth 2.

For a chosen delay `d = D - 2`, use the carrier

`Y_d = X x {0, ..., d}`.

Lift each base law `f_i` to

`F_i(x, r) = (f_i(x), d)`.

Define the common intervention

`T(x, r) = (x, r-1)` for `r > 0`,

and

`T(x, 0) = (N(x), 0)`.

After `t <= d` intervention steps,

`T^t F_i(x, r) = (f_i(x), d-t)`.

Thus all disagreements and their compatible closure live inside one active layer and are isomorphic to the base depth-0 common-law closure. All other states are singleton congruence classes.

At depth `d+1`, the active layer reaches 0 and one application of `N` has occurred, so the closure is the base depth-1 closure. At depth `d+2`, it is the base depth-2 closure, where the two base systems separate.

Therefore the first separation occurs at

`D = d + 2`.

### Cost scaling

If the base carrier has size 5 and the delayed system has `d+1` layers, only one layer contains non-singleton congruence classes. Consequently the uniform Law Genesis Cost is divided by `d+1`.

At the separating depth,

`Gamma_A_D = ((3/5) log2(3)) / (d+1)`,

while

`Gamma_B_D = 0.4 / (d+1)`.

The gap remains nonzero for every finite `d`.

### Status and novelty boundary

Status: exact constructive theorem, with regression tests for multiple delays and generated machine-readable results.

The delay-line device itself is not claimed as a new automata or semigroup mechanism. Its role is narrower: it converts the finite nonlinear common-law witness into an arbitrary-depth Law-Genesis separation family. The remaining novelty question is whether a non-artificial family exists whose depth growth follows from intrinsic nonlinear common-law closure rather than an explicit delay gadget.
