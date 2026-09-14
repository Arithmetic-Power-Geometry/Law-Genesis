# Law Genesis Theorems

This file records theorem statements that are supported either by direct proof or by an explicit finite verification. Standard machinery is identified separately from framework-specific interpretation.

## Common-Law Congruence Representation

Let `F = {f1, ..., fm}` be deterministic maps on a finite set `X`. Let `R_F` contain every pair `(fi(x), fj(x))`. A quotient `q : X -> Y` supports a single map `G : Y -> Y` satisfying `q fi = G q` for every `i` if and only if `ker(q)` is a congruence for all maps in `F` and contains `R_F`. Therefore the finest valid common-law quotient is `X / Theta_F`, where `Theta_F` is the least such congruence.

This is an application of standard generated-congruence machinery to the common-law constraint.

## Fixed Raw-Disagreement Separation

### Statement

There exist two finite three-law systems `A` and `B` on the same five-state carrier such that their raw disagreement relations are exactly equal,

`R_A = R_B`,

but their least common-law congruences are different and therefore their Law Genesis Costs are different.

For the explicit depth-2 transformed witness in `examples/nonlinear_depth_witness.py`, both systems have

`R_A = R_B = {(0,2)}`.

Nevertheless,

`Theta_A = {{0,1,2},{3},{4}}`,

while

`Theta_B = {{0,2},{1},{3},{4}}`.

Therefore

`Gamma(A) = (3/5) log2(3)`,

whereas

`Gamma(B) = 2/5 = 0.4` bits.

Hence the raw microscopic disagreement relation alone does not determine the dynamically compatible abstraction forced by those disagreements.

### Direct proof for the explicit pair

For System A at the separating depth, the transformed laws are

`a1 = (1,0,0,0,2)`,

`a2 = (1,2,2,0,0)`,

`a3 = (1,0,0,0,0)`.

The only raw disagreement pair is `0 ~ 2`. Compatibility with `a1` then forces

`a1(0)=1 ~ a1(2)=0`,

so `0,1,2` must lie in one congruence class. No further identification with states 3 or 4 is forced. Thus the least common-law congruence has class sizes `(3,1,1)`.

For System B at the same depth, the transformed laws are

`b1 = (0,1,0,2,0)`,

`b2 = (2,1,0,0,0)`,

`b3 = (0,1,0,0,2)`.

Again the only raw disagreement pair is `0 ~ 2`. Under each transformed law, the images of 0 and 2 remain inside the pair `{0,2}`. Therefore congruence closure forces no third state into the block, and the least common-law congruence has class sizes `(2,1,1,1)`.

### Strengthened sequential form

For the same original systems and common intervention `N`, the exact raw disagreement relations agree at every observed depth through the separating depth:

- depth 0: `{(0,1),(0,2),(0,4),(1,2),(1,4),(2,4)}`;
- depth 1: `{(0,1),(0,3),(1,3)}`;
- depth 2: `{(0,2)}`.

The least common-law congruence partitions also agree at depths 0 and 1, but differ at depth 2. Thus the separation is not caused by different raw disagreement sets; it is caused by different propagation of the same disagreement relation under dynamical compatibility.

### Status and novelty boundary

Status: exact finite theorem with a direct proof and regression test.

Generated congruence closure itself is standard universal algebra. The framework-specific content is the separation between raw law disagreement and the information cost of the least dynamically compatible common-law quotient. This theorem should therefore be presented as a structural Law-Genesis separation result, not as a claim that congruence generation is new.

## Intrinsic Clock-Free Depth Separation Witness

### Explicit witness

On the four-state carrier `X={0,1,2,3}`, use the common intervention

`P = (1,2,3,0)`,

which is a 4-cycle and therefore has no transient countdown states.

System A consists of

`a1=(3,2,1,3)`,

`a2=(3,0,3,3)`,

`a3=(0,2,1,1)`.

System B consists of

`b1=(2,2,3,0)`,

`b2=(0,2,3,1)`,

`b3=(1,0,3,2)`.

For depths `t=0,1,2`, the two systems match on:

- Law Genesis Cost `Gamma`;
- common-law congruence class-size profile;
- raw disagreement-pair count;
- critical seed rank `beta`;
- complete one-seed fragility spectrum.

For all three matched depths,

`Gamma_A(t)=Gamma_B(t)=2` bits.

At depth 3, however,

`Gamma_A(3)=2`,

while

`Gamma_B(3)=1.188721875541...` bits.

Thus a depth-3 Law-Genesis separation exists without an explicit delay-line intervention.

### Status and novelty boundary

Status: deterministic computational witness, frozen in `examples/intrinsic_depth_witness.py` and regression-tested in `tests/test_intrinsic_depth_witness.py`.

This is stronger than the explicit delay-lift construction because the shared intervention is a permutation. It is not yet an arbitrary-depth intrinsic theorem. The current open theorem target is a family whose first separating depth grows unboundedly without introducing delay layers or equivalent clock structure.

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
