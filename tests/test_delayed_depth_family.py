from math import isclose, log2

from examples.delayed_depth_family import build_delayed_pair, diagnostics, verify_depth_family


def test_delayed_family_matches_then_separates_for_small_delays():
    for delay in range(5):
        result = verify_depth_family(delay)
        assert result["all_prior_observables_match"]
        assert result["separates_in_gamma"]
        assert result["separating_depth"] == delay + 2


def test_separation_cost_scales_by_number_of_layers():
    for delay in range(4):
        pair = build_delayed_pair(delay)
        depth = delay + 2
        a = diagnostics(pair, "A", depth)
        b = diagnostics(pair, "B", depth)
        scale = delay + 1
        expected_a = ((3 / 5) * log2(3)) / scale
        expected_b = 0.4 / scale
        assert isclose(a["gamma_bits"], expected_a, rel_tol=1e-12, abs_tol=1e-12)
        assert isclose(b["gamma_bits"], expected_b, rel_tol=1e-12, abs_tol=1e-12)


def test_same_intervention_and_same_prior_profiles():
    pair = build_delayed_pair(3)
    assert pair.intervention == pair.intervention
    for depth in range(pair.separating_depth):
        a = diagnostics(pair, "A", depth)
        b = diagnostics(pair, "B", depth)
        assert isclose(a["gamma_bits"], b["gamma_bits"], rel_tol=1e-12, abs_tol=1e-12)
        assert a["class_sizes"] == b["class_sizes"]
        assert a["raw_disagreement_pairs"] == b["raw_disagreement_pairs"]
