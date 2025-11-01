class FormatError(Exception):
    """Raised when data format is incorrect."""
    pass


class ValidationError(Exception):
    """Raised when value fails validation."""
    pass