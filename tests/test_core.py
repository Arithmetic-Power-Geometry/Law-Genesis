from math import isclose, log2

from law_genesis.core import (
    class_sizes,
    disagreement_pairs,
    entropy_loss_uniform,
    least_common_law_congruence,
    law_genesis_cost_uniform,
)


def test_identical_laws_have_zero_cost():
    f = (1, 2, 0)
    assert disagreement_pairs((f, f)) == set()
    assert least_common_law_congruence((f, f)) == ((0,), (1,), (2,))
    assert law_genesis_cost_uniform((f, f)) == 0.0


def test_identity_and_constant_force_universal_congruence():
    identity = (0, 1, 2, 3)
    constant = (0, 0, 0, 0)
    part = least_common_law_congruence((identity, constant))
    assert class_sizes(part) == (4,)
    assert isclose(law_genesis_cost_uniform((identity, constant)), log2(4))


def test_entropy_loss_from_class_sizes():
    part = ((0, 1, 2), (3,), (4,))
    expected = (3 / 5) * log2(3)
    assert isclose(entropy_loss_uniform(part), expected, rel_tol=1e-12, abs_tol=1e-12)
