from .validator import validate_length, validate_positive, validate_currency
from .errors import ValidationError
from .constants import CURRENCIES

def get_validated_length(usertext: str, field: str) -> str:
    """Ask user for value and check it."""
    while True:
        value = input(usertext).strip()
        try:
            if field:
                validate_length(field, value)
            return value
        except ValidationError:
            print("The input is incorrect. Try again.")
                
def get_validated_amount(usertext: str) -> float:
    """Ask user for amount and check it."""
    while True:
        try:
            value = get_validated_length(usertext, "amount")
            amount = float(value)
            validate_positive(amount)
            return amount
        except ValueError:
            print("The amount is incorrect. Try again.")
        except ValidationError:
            print("The amount is incorrect. Try again.")

def get_validated_currency(usertext: str) -> str:
    """Ask user for currency and check it."""
    while True:
        print(f"Available currencies: {', '.join((CURRENCIES))}")
        currency = input(usertext).strip().upper()
        try:
            validate_currency(currency)
            return currency
        except ValidationError:
            print("The currency is incorrect. Try again.")