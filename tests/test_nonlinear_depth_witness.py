from math import isclose, log2

from examples.nonlinear_depth_witness import INTERVENTIONS, SYSTEM_A, SYSTEM_B
from law_genesis.core import (
    apply_word,
    class_sizes,
    disagreement_pairs,
    least_common_law_congruence,
    law_genesis_cost_uniform,
    protocol_cost_uniform,
    raw_disagreement_count,
)


def transformed(system, depth):
    if depth == 0:
        return system
    word = "N" * depth
    return tuple(apply_word(law, INTERVENTIONS, word) for law in system)


def test_depth_zero_and_one_match():
    assert isclose(law_genesis_cost_uniform(SYSTEM_A), log2(5), rel_tol=1e-12)
    assert isclose(law_genesis_cost_uniform(SYSTEM_B), log2(5), rel_tol=1e-12)

    a1 = protocol_cost_uniform(SYSTEM_A, INTERVENTIONS, "N")
    b1 = protocol_cost_uniform(SYSTEM_B, INTERVENTIONS, "N")
    assert isclose(a1, 1.6, rel_tol=1e-12, abs_tol=1e-12)
    assert isclose(b1, 1.6, rel_tol=1e-12, abs_tol=1e-12)


def test_depth_two_separates():
    a2 = protocol_cost_uniform(SYSTEM_A, INTERVENTIONS, "NN")
    b2 = protocol_cost_uniform(SYSTEM_B, INTERVENTIONS, "NN")
    assert isclose(a2, (3 / 5) * log2(3), rel_tol=1e-12, abs_tol=1e-12)
    assert isclose(b2, 0.4, rel_tol=1e-12, abs_tol=1e-12)
    assert not isclose(a2, b2)


def test_expected_class_profiles():
    expected_a = [(5,), (4, 1), (3, 1, 1)]
    expected_b = [(5,), (4, 1), (2, 1, 1, 1)]
    for depth in range(3):
        pa = least_common_law_congruence(transformed(SYSTEM_A, depth))
        pb = least_common_law_congruence(transformed(SYSTEM_B, depth))
        assert class_sizes(pa) == expected_a[depth]
        assert class_sizes(pb) == expected_b[depth]


def test_exact_raw_disagreement_relations_match_through_separation():
    expected = [
        {(0, 1), (0, 2), (0, 4), (1, 2), (1, 4), (2, 4)},
        {(0, 1), (0, 3), (1, 3)},
        {(0, 2)},
    ]
    for depth in range(3):
        a = transformed(SYSTEM_A, depth)
        b = transformed(SYSTEM_B, depth)
        assert disagreement_pairs(a) == expected[depth]
        assert disagreement_pairs(b) == expected[depth]
        assert raw_disagreement_count(a) == raw_disagreement_count(b)
