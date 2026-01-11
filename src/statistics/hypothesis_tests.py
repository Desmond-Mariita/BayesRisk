"""
Hypothesis testing framework implemented from scratch.

This module provides statistical tests without using scipy.stats.
This directly addresses the BSc weakness in "Tests of Hypothesis I".

Mathematical Background:
------------------------
Two-Sample t-Test (Welch's):
    t = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂)

Degrees of freedom (Welch-Satterthwaite):
    df = (s₁²/n₁ + s₂²/n₂)² / [(s₁²/n₁)²/(n₁-1) + (s₂²/n₂)²/(n₂-1)]

Chi-Square Test:
    χ² = Σᵢⱼ (Oᵢⱼ - Eᵢⱼ)² / Eᵢⱼ
"""

from typing import Tuple

import numpy as np


def welch_ttest(
    group1: np.ndarray,
    group2: np.ndarray,
) -> Tuple[float, float, float]:
    """
    Perform Welch's t-test for two independent samples.

    Why Welch's over Student's t-test?
        Student's t-test assumes equal variances. In credit data,
        defaulters and non-defaulters often have different variance
        in income, debt ratios, etc. Welch's is robust to this.

    Formula:
        t = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂)

    Args:
        group1: Observations from first group (e.g., defaulters).
        group2: Observations from second group (e.g., non-defaulters).

    Returns:
        Tuple of (t_statistic, degrees_of_freedom, p_value).

    Example:
        >>> defaults = loan_amount[loan_status == 'Default']
        >>> non_defaults = loan_amount[loan_status == 'Paid']
        >>> t, df, p = welch_ttest(defaults, non_defaults)
        >>> if p < 0.05:
        ...     print("Significant difference in loan amounts")
    """
    # TODO: Implement in Week 6
    # This directly addresses your BSc gap!
    raise NotImplementedError("Implement this function in Week 6")


def chi_squared_test(
    observed: np.ndarray,
    expected: np.ndarray = None,
) -> Tuple[float, float, int]:
    """
    Perform chi-squared test for independence.

    Formula: χ² = Σᵢⱼ (Oᵢⱼ - Eᵢⱼ)² / Eᵢⱼ

    Args:
        observed: Contingency table of observed frequencies.
        expected: Expected frequencies. If None, calculated from marginals.

    Returns:
        Tuple of (chi2_statistic, p_value, degrees_of_freedom).
    """
    # TODO: Implement in Week 6
    raise NotImplementedError("Implement this function in Week 6")


def z_test_proportion(
    successes1: int,
    n1: int,
    successes2: int,
    n2: int,
) -> Tuple[float, float]:
    """
    Perform z-test for comparing two proportions.

    Example use: "Is the default rate different for Grade A vs Grade B loans?"

    Args:
        successes1: Number of successes (e.g., defaults) in group 1.
        n1: Total observations in group 1.
        successes2: Number of successes in group 2.
        n2: Total observations in group 2.

    Returns:
        Tuple of (z_statistic, p_value).
    """
    # TODO: Implement in Week 6
    raise NotImplementedError("Implement this function in Week 6")


def calculate_p_value_from_t(t_stat: float, df: float) -> float:
    """
    Calculate two-tailed p-value from t-statistic.

    Uses numerical approximation of the t-distribution CDF.

    Args:
        t_stat: t-statistic value.
        df: Degrees of freedom.

    Returns:
        Two-tailed p-value.

    Note:
        This requires implementing the t-distribution CDF,
        which involves the incomplete beta function.
        For Week 6, you may use a lookup table or approximation.
    """
    # TODO: Implement in Week 6
    raise NotImplementedError("Implement this function in Week 6")
