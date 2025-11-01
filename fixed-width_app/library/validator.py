from .constants import (
    FIELD_LIMITS,
    CURRENCIES,
    T_MAX,
    LINE_LEN
)
from .errors import ValidationError, FormatError
from .models import Transaction

def calculate_width(interval: tuple[int, int]) -> int:
    """Return the width of field interval."""
    start, end = interval
    return end - start + 1

def validate_required(value: str) -> None:
    """Ensure the value is not empty."""
    if value is None or str(value).strip() == "":
        raise ValidationError(f"This field cannot be empty.")

def validate_length(field: str, value: str) -> None:
    """Validate text length for field."""
    validate_required(value)
    if field not in FIELD_LIMITS:
        return
    limit = calculate_width(FIELD_LIMITS[field])
    if len(str(value)) > limit:
        raise ValidationError(f"Value is too long, try again.")
    
def validate_currency(currency: str) -> None:
    """Verify currency is supported."""
    if currency not in CURRENCIES:
        raise ValidationError("Choose the currency from"
                              f"{', '.join(CURRENCIES)}")
    
def validate_transaction_limit(transactions: list[Transaction]) -> None:
    """Check the number of transactions."""
    if not (1 <= len(transactions) <= T_MAX):
        raise ValidationError(f"Transaction limit has been reached.")
    
def validate_counter(counter: int) -> None:
    """Verify counter is within transactions range."""
    if not (1 <= counter <= T_MAX):
        raise ValidationError(f"Transaction limit has been reached.")
    
def validate_positive(num: float) -> None:
    """Reject zero or negative numbers."""
    if num <= 0:
        raise ValidationError(f"Amount or sum must be positive")
    
def validate_empty_file(lines: list[str]) -> None:
    """Ensure the file is not empty."""
    if not lines:
        raise FormatError(f"No lines to write.")
    
def validate_digit(smth: str) -> None:
    """Verify input is numeric."""
    if not smth.isdigit():
        raise FormatError(f"It is not numeric.")
    
def validate_id(line: str, expected: str) -> None:
    """Check ID of the line."""
    id = line[:2]
    if id != expected:
        raise FormatError(f"Not expected ID.")
    
def validate_line_len(line: str) -> None:
    """Check fixed-width line size."""
    if len(line) != LINE_LEN:
        raise FormatError(f"Invalid string length")