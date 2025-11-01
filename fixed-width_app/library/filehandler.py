from pathlib import Path

from .models import Header, Transaction, Footer
from .encode import encode_header, encode_transaction, encode_footer
from .decode import decode_header, decode_transaction, decode_footer
from .validator import validate_empty_file, validate_line_len

def read_file (path: str | Path) -> tuple[Header, list[Transaction], Footer]:
    """Read and decode data from a structured file."""
    filename = Path(path)

    lines: list[str] = []
    with open(filename, 'r', encoding='UTF-8') as file:
        while line := file.readline():
            line = line.lstrip().rstrip('\r\n')
            validate_line_len(line)
            lines += (line,)
    validate_empty_file(lines)
        
    header = decode_header(lines[0])
    footer = decode_footer(lines[-1])
    transactions = []
    for line in lines[1:-1]:
        transaction = decode_transaction(line)
        transactions.append(transaction)
        
    return header, transactions, footer

def write_file(
    path: str | Path,
    header: Header,
    transactions: list[Transaction],
    footer: Footer
) -> None:
    """Write and encode data to a structured file."""
    filename = Path(path)

    lines: list[str] = []
    lines = [encode_header(header)]
    for transaction in transactions:
        lines.append(encode_transaction(transaction))
    lines.append(encode_footer(footer))

    validate_empty_file(lines) 
    for line in lines:
        validate_line_len(str(line))

    with open(filename, 'w', encoding='UTF-8') as file:
        file.write("\n".join(lines) + "\n")