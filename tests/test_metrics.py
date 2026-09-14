from math import isclose, log2

from examples.fragility_separation import build_systems
from law_genesis.core import forced_abstraction_uniform
from law_genesis.metrics import (
    critical_seed_rank,
    genesis_work_uniform,
    interaction_uniform,
    protocol_profile_uniform,
)


def test_critical_seed_rank_separation_family():
    for n in range(2, 7):
        system_a, system_b = build_systems(n)
        assert critical_seed_rank(system_a) == 1
        assert critical_seed_rank(system_b) == n - 1


def test_forced_abstraction_cycle_seed_is_maximal_for_n4():
    system_a, _ = build_systems(4)
    fa = forced_abstraction_uniform(system_a, ((0, 1),))
    direct_loss = 0.5  # one block of size 2 under the uniform distribution on 4 states
    assert isclose(fa, log2(4) - direct_loss, rel_tol=1e-12, abs_tol=1e-12)


def test_interaction_can_be_computed_exactly():
    _, system_b = build_systems(4)
    sigma = interaction_uniform(system_b, ((0, 1),), ((1, 2),))
    assert isinstance(sigma, float)


def test_protocol_profile_and_work_agree():
    identity = (0, 1, 2)
    constant = (0, 0, 0)
    intervention = {"P": (0, 0, 2)}
    laws = (identity, constant)
    profile = protocol_profile_uniform(laws, intervention, "PP", include_initial=False)
    work = genesis_work_uniform(laws, intervention, "PP", include_initial=False)
    assert isclose(work, sum(profile), rel_tol=1e-12, abs_tol=1e-12)
