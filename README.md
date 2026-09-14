# Law Genesis

A reproducible framework for studying how multiple microscopic laws can become one reusable effective law through controlled abstraction.

The project was developed from a theory-first workflow: definitions and theorem targets were written first, then software was created to verify the constructions, search for counterexamples, and separate genuinely new results from reductions to established mathematics.

## Core objects

For a finite state space `X` and microscopic laws `F = {f1, ..., fm}`, define the raw disagreement relation

`R_F = {(fi(x), fj(x)) : x in X, i, j}`.

The least common-law congruence `Theta_F` is the least congruence containing `R_F` and compatible with all laws in `F`.

The finest quotient on which all microscopic laws induce one reusable effective law is

`X / Theta_F`.

For a distribution on `X`, the Law Genesis Cost is

`Gamma(F) = H(X | X/Theta_F)`.

For the uniform finite case, the package computes this directly from congruence-class sizes.

## What the software does

The implementation can:

- compute raw disagreement pairs;
- compute the least common-law congruence;
- compute Law Genesis Cost for uniform finite systems;
- apply intervention words and evaluate protocol-conditioned Law Genesis Cost;
- compute forced-abstraction loss for designated seed identifications;
- compute a critical seed rank for finite systems;
- reproduce the nonlinear three-law depth witness used in the current theory development;
- run automated tests intended as falsification checks rather than demonstrations only.

## Theory boundary

The repository deliberately separates framework claims from established machinery. Generated congruences are standard universal algebra. In linear systems, the least invariant closure underlying Law Genesis reduces to classical reachability/invariant-subspace constructions. Matrix-word depth, Jordan/Weyr phenomena, matroid dependence, and Min-Sum Set Cover are treated as existing mathematics and are not claimed as new mechanisms here.

The present research question is narrower:

> How much state distinction must be surrendered before several microscopic laws can become one reusable effective law, and how can that cost differ from simple disagreement magnitude or ordinary low-order summaries?

## Reproduce

```bash
python -m pip install -e .
pytest -q
python scripts/reproduce.py
```

The reproduction script writes machine-readable results to `results/`.

## Repository structure

- `law_genesis/` — core implementation
- `examples/` — explicit finite constructions
- `scripts/` — reproduction and search utilities
- `tests/` — theorem and regression tests
- `results/` — generated result tables
- `.github/workflows/` — continuous integration

## Status

This repository is a research artifact for a developing foundations project. A passing computational test is evidence that an implementation matches the stated finite construction; it is not, by itself, a proof of mathematical novelty.

## License

Apache License 2.0.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
