"""
helpers.py
Utility functions for directory handling and file paths.
"""

from pathlib import Path


def get_project_root():
    """
    Automatically detect the project root directory.
    (The folder where README.md is located)
    """
    current = Path(__file__).resolve()

    while True:
        if (current / "README.md").exists():
            return current
        if current.parent == current:
            break
        current = current.parent

    return Path(__file__).resolve().parent.parent


def get_data_dir():
    """
    Return the path to the data/ directory.
    Ensures data/raw and data/processed exist.
    """
    root = get_project_root()
    data_dir = root / "data"

    # auto-create directories
    (data_dir / "raw").mkdir(parents=True, exist_ok=True)
    (data_dir / "processed").mkdir(parents=True, exist_ok=True)

    return data_dir
