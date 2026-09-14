"""Law Genesis finite-system analysis tools."""

from .core import (
    disagreement_pairs,
    least_common_law_congruence,
    law_genesis_cost_uniform,
    apply_word,
)

__all__ = [
    "disagreement_pairs",
    "least_common_law_congruence",
    "law_genesis_cost_uniform",
    "apply_word",
]

__version__ = "0.1.0"
