"""
Data acquisition utilities for downloading and caching datasets.

This module handles downloading the Lending Club dataset from various sources.
"""

from pathlib import Path
from typing import Optional

# =============================================================================
# CONSTANTS
# =============================================================================
KAGGLE_DATASET = "wordsforthewise/lending-club"
DATA_DIR = Path(__file__).parent.parent.parent / "data" / "raw"


def download_from_kaggle(
    dataset_name: str = KAGGLE_DATASET,
    output_dir: Optional[Path] = None,
) -> Path:
    """
    Download dataset from Kaggle.

    Args:
        dataset_name: Kaggle dataset identifier (user/dataset-name).
        output_dir: Directory to save the downloaded files.

    Returns:
        Path to the downloaded file.

    Raises:
        EnvironmentError: If Kaggle API credentials are not configured.
        ConnectionError: If download fails.

    Note:
        Requires Kaggle API credentials in ~/.kaggle/kaggle.json
    """
    # TODO: Implement in Week 1
    raise NotImplementedError("Implement this function in Week 1")
