"""Errors for AI Run Community Tools."""


class TruncatedOutputError(Exception):
    """Error raised when output is truncated due to token limit."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)