"""
Data loading utilities for the BayesRisk project.

This module provides functions to load and validate the Lending Club dataset.
"""

from pathlib import Path
from typing import Optional, Tuple, Union

import numpy as np
import pandas as pd

# =============================================================================
# CONSTANTS
# =============================================================================
DEFAULT_DATA_PATH = Path(__file__).parent.parent.parent / "data" / "raw"
TARGET_COLUMN = "loan_status"
DEFAULT_DTYPES = {
    "id": str,
    "member_id": str,
    "loan_amnt": float,
    "funded_amnt": float,
    "term": str,
    "int_rate": str,
    "grade": str,
    "sub_grade": str,
}


def load_lending_club_data(
    filepath: Optional[Union[str, Path]] = None,
    nrows: Optional[int] = None,
    usecols: Optional[list] = None,
) -> pd.DataFrame:
    """
    Load the Lending Club loan dataset.

    Args:
        filepath: Path to the CSV file. If None, looks in default data directory.
        nrows: Number of rows to load. If None, loads all rows.
        usecols: List of columns to load. If None, loads all columns.

    Returns:
        DataFrame containing the loan data.

    Raises:
        FileNotFoundError: If the data file is not found.
        ValueError: If the file is empty or corrupted.

    Example:
        >>> df = load_lending_club_data(nrows=1000)
        >>> print(df.shape)
        (1000, 150)
    """
    # TODO: Implement in Week 1
    raise NotImplementedError("Implement this function in Week 1")


def validate_data(df: pd.DataFrame) -> Tuple[bool, list]:
    """
    Validate the loaded dataset for expected structure and content.

    Args:
        df: DataFrame to validate.

    Returns:
        Tuple of (is_valid, list_of_issues).

    Raises:
        TypeError: If input is not a DataFrame.
    """
    # TODO: Implement in Week 1
    raise NotImplementedError("Implement this function in Week 1")


def get_data_summary(df: pd.DataFrame) -> dict:
    """
    Generate a summary of the dataset.

    Args:
        df: DataFrame to summarize.

    Returns:
        Dictionary containing shape, dtypes, memory usage, etc.
    """
    # TODO: Implement in Week 1
    raise NotImplementedError("Implement this function in Week 1")
