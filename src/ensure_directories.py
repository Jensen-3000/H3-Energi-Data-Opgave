import os
from config import OUTPUT_DIR, RESULTS_DIR


def ensure_directories():
    """
    Ensure that output and results directories exist.

    Creates the directories if they do not already exist.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)
