"""Utilities for AI Run Community Tools."""
import re


def sanitize_string(text: str) -> str:
    """Sanitize string from special characters."""
    if not text:
        return ""
    # Remove ANSI escape sequences
    text = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', text)
    return text.strip()