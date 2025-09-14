"""
Utility functions for hashing and related operations.
"""

import hashlib

def hash_text(text: str) -> str:
    """
    Generates a SHA-256 hash for the given text.
    Args:
        text (str): The input text to hash.
    Returns:
        str: The resulting SHA-256 hash in hexadecimal format.
    """
    return hashlib.sha256(text.encode()).hexdigest()
