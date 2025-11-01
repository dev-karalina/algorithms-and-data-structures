from .constants import (
    H_ID, T_ID, F_ID,
    H_NAME, H_SURNAME, H_PATRONYMIC, H_ADDRESS,
    T_COUNTER, T_AMOUNT, T_CURRENCY,
    F_COUNTER, F_SUM
)
from .models import Header, Transaction, Footer
from .validator import (
    validate_counter,
    validate_currency,
    validate_digit,
    validate_id,
    validate_line_len
)

def slice_field (line: str, interval: tuple[int, int]) -> str:
    """Cut a substring using coordinates."""
    validate_line_len(line)
    start, end = interval
    return line[start - 1: end]

def decode_header(line: str) -> Header:
    """Decode a header record line into a Header object."""
    validate_id(line, H_ID)
    return Header(
        name=slice_field(line, H_NAME).lstrip(" "),
        surname=slice_field(line, H_SURNAME).lstrip(" "),
        patronymic=slice_field(line, H_PATRONYMIC).lstrip(" "),
        address=slice_field(line, H_ADDRESS).lstrip(" "),
    )

def decode_transaction(line: str) -> Transaction:
    """Decode a transaction record line into a Transaction object."""
    validate_id(line, T_ID)

    counter_str = slice_field(line, T_COUNTER)
    validate_digit(counter_str)
    counter_int = int(counter_str)
    validate_counter(counter_int)
    
    amount_str = slice_field(line, T_AMOUNT)
    validate_digit(amount_str)
    
    currency_str = slice_field(line, T_CURRENCY).lstrip(" ")
    validate_currency(currency_str)

    return Transaction(
        counter=counter_int,
        amount=int(amount_str) / 100.0,
        currency=currency_str,
    )

def decode_footer(line: str) -> Footer:
    """Decode a footer record line into a Footer object."""
    validate_id(line, F_ID)

    counter_str = slice_field(line, F_COUNTER)
    validate_digit(counter_str)
    counter_int = int(counter_str)
    validate_counter(counter_int)
    
    sum_str = slice_field(line, F_SUM)
    validate_digit(sum_str)
    
    return Footer(
        counter=counter_int,
        sum=int(sum_str) / 100.0,
    )