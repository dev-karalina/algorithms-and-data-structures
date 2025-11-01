from library.models import Header, Transaction, Footer

WINDOW_WIDTH = 45
LINE = "-" * WINDOW_WIDTH

def section(title: str) -> None:
    """Display the section title."""
    print(f"\n{LINE}\n{title:^45}\n{LINE}")

def show_header(header: Header) -> None:
    """Display all header fields."""
    section("File Header")
    print(f"Name: {header.name}")
    print(f"Surname: {header.surname}")
    print(f"Patronymic: {header.patronymic}")
    print(f"Address: {header.address}")
    print(f"{LINE}")

def show_transactions(transactions: list[Transaction]) -> None:
    """Display all transactions in readable format."""
    section("Transactions")
    if not transactions:
        print("There are no transactions in the file.")
    else:
        for i, t in enumerate(transactions, start=1):
            print(
                f"Nr. {i:<3} "
                f"Amount: {t.amount:<12.2f} "
                f"Currency: {t.currency}"
            )
    print(f"{LINE}")

def show_footer(footer: Footer) -> None:
    """Display all footer fields."""
    print(f"Total transactions: {footer.counter}")
    print(f"Control sum: {footer.sum}")
    print(f"{LINE}")