from .constants import (
    LINE_LEN, H_ID, T_ID, F_ID,
    H_NAME, H_SURNAME, H_PATRONYMIC, H_ADDRESS,
    T_COUNTER, T_AMOUNT, T_CURRENCY,
    F_COUNTER, F_SUM
)
from .models import Header, Transaction, Footer
from .validator import (
    calculate_width,
    validate_counter,
    validate_currency,
    validate_positive
)

def fill_left(content: str | None, width: int, fillchar: str = " ") -> str:
    """Right align text and fill remaining with the character."""
    if content is None:
        content = ""
    content = str(content)[:width]
    return content.rjust(width, fillchar)

def fill_line_len(initial: str) -> str:
    """Ensure the line reaches required length."""
    gap = LINE_LEN - len(initial)
    if gap >= 0:
        return initial + " " * gap

def encode_header(content: Header) -> str:
    """Encode a Header object into a fixed-wisth string."""
    parts = (
        H_ID,
        fill_left(content.name, calculate_width(H_NAME)),
        fill_left(content.surname, calculate_width(H_SURNAME)),
        fill_left(content.patronymic, calculate_width(H_PATRONYMIC)),
        fill_left(content.address, calculate_width(H_ADDRESS)),
    )
    return fill_line_len("".join(parts))

def encode_transaction(content: Transaction) -> str:
    """Encode a Transaction object into a fixed-wisth string."""
    validate_currency(content.currency)
    validate_counter(int(content.counter))
    content.amount = int(float(content.amount) * 100)
    validate_positive(content.amount)
    
    parts = (
        T_ID,
        fill_left(str(content.counter), calculate_width(T_COUNTER), "0"),
        fill_left(str(content.amount), calculate_width(T_AMOUNT), "0"),
        fill_left(content.currency, calculate_width(T_CURRENCY)),
    )
    return fill_line_len("".join(parts))

def encode_footer(content: Footer) -> str:
    """Encode a Footer object into a fixed-wisth string."""
    validate_counter(content.counter)
    content.sum = int(float(content.sum) * 100)
    validate_positive(content.sum)
    
    parts = (
        F_ID,
        fill_left(str(content.counter), calculate_width(F_COUNTER), "0"),
        fill_left(str(content.sum), calculate_width(F_SUM), "0"),
    )
    return fill_line_len("".join(parts))