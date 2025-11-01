from .models import Header, Transaction, Footer
from .filehandler import write_file
from .validator import (
    validate_counter,
    validate_currency,
    validate_length,
    validate_positive
)
from .locks import blocked

def add_transaction(
    transactions: list[Transaction],
    footer: Footer,
    header: Header,
    amount: float,
    currency: str
) -> Transaction | None:
    """Append a new transaction and update the file."""
    validate_currency(currency)
    counter_int = len(transactions) + 1
    validate_counter(counter_int)
    validate_positive(amount)
    validate_length("amount", amount)
    if (
        blocked("transaction[*].amount")
        or blocked("transaction[*].currency")
    ):
        return None
    
    new = Transaction(
        counter=str(counter_int),
        amount=amount,
        currency=currency,
    )

    transactions.append(new)
    footer.counter = len(transactions)
    total_sum = 0
    for transaction in transactions:
        total_sum += transaction.amount
    footer.sum = total_sum
    write_file("data.txt", header, transactions, footer)
    return new

def get_field(
    header: Header,
    transactions: list[Transaction],
    footer: Footer,
    path: str
):
    """Read the value from selected field."""
    if path.startswith("header."):
        return getattr(header, path.removeprefix("header."))
    elif path.startswith("footer."):
        return getattr(footer, path.removeprefix("footer."))
    elif path.startswith("transactions["):
        content = path[len("transactions["):].split("].", 1)
        index_str, field = content
        index = int(index_str) - 1
        return getattr(transactions[index], field)
    
def set_field(
    header: Header,
    transactions: list[Transaction],
    footer: Footer,
    path: str,
    value: str
):
    """Set the value to selected field."""
    if path.startswith("header."):
        field = path.removeprefix("header.")
        validate_length(field, value)
        setattr(header, field, value)
        write_file("data.txt", header, transactions, footer)
        return getattr(header, field)
    
    elif path.startswith("footer."):
        field = path.removeprefix("footer.")
        if field in ("counter", "sum"):
            raise PermissionError("This field is read-only.")
    
    elif path.startswith("transactions["):
        content = path[len("transactions["):].split("].", 1)
        index_str, field = content
        index = int(index_str) - 1
        transaction = transactions[index]
        if field == "counter":
            raise PermissionError("This field is read-only.")
        elif field == "amount":
            setattr(transaction, field, float(value))
            total_sum = 0
            for transaction in transactions:
                total_sum += transaction.amount
            footer.sum = total_sum
            write_file("data.txt", header, transactions, footer)
            return transaction.amount
        elif field == "currency":
            validate_currency(value)
            setattr(transaction, field, value)
            write_file("data.txt", header, transactions, footer)
            return transaction.currency