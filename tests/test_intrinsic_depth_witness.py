from math import isclose

from examples.intrinsic_depth_witness import SYSTEM_A, SYSTEM_B, diagnostics


def test_intrinsic_witness_matches_through_depth_two():
    for depth in range(3):
        a = diagnostics(SYSTEM_A, depth)
        b = diagnostics(SYSTEM_B, depth)
        assert isclose(a["gamma_bits"], b["gamma_bits"], rel_tol=1e-12, abs_tol=1e-12)
        assert a["class_sizes"] == b["class_sizes"]
        assert a["raw_disagreement_count"] == b["raw_disagreement_count"]
        assert a["beta"] == b["beta"]
        assert a["fragility_order1"] == b["fragility_order1"]


def test_intrinsic_witness_separates_at_depth_three():
    a = diagnostics(SYSTEM_A, 3)
    b = diagnostics(SYSTEM_B, 3)
    assert isclose(a["gamma_bits"], 2.0, rel_tol=1e-12, abs_tol=1e-12)
    assert isclose(b["gamma_bits"], 1.188721875540867, rel_tol=1e-12, abs_tol=1e-12)
    assert not isclose(a["gamma_bits"], b["gamma_bits"], rel_tol=1e-12, abs_tol=1e-12)
