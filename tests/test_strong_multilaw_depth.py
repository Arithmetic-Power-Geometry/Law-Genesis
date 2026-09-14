from math import isclose

from examples.nonlinear_depth_witness import SYSTEM_A, SYSTEM_B, summary


def test_low_depth_observables_match_before_separation():
    a = summary(SYSTEM_A)
    b = summary(SYSTEM_B)

    for depth in (0, 1):
        assert isclose(a[depth]["gamma_bits"], b[depth]["gamma_bits"], rel_tol=1e-12, abs_tol=1e-12)
        assert a[depth]["class_sizes"] == b[depth]["class_sizes"]
        assert a[depth]["raw_disagreement_pairs"] == b[depth]["raw_disagreement_pairs"]
        assert a[depth]["beta"] == b[depth]["beta"]
        assert a[depth]["fragility_order1"] == b[depth]["fragility_order1"]


def test_next_depth_separates_despite_matching_raw_count_and_beta():
    a = summary(SYSTEM_A)
    b = summary(SYSTEM_B)

    assert a[2]["raw_disagreement_pairs"] == b[2]["raw_disagreement_pairs"] == 1
    assert a[2]["beta"] == b[2]["beta"] == 2
    assert a[2]["class_sizes"] != b[2]["class_sizes"]
    assert not isclose(a[2]["gamma_bits"], b[2]["gamma_bits"], rel_tol=1e-12, abs_tol=1e-12)
