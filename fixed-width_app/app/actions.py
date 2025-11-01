import time

from library.filehandler import write_file
from library.models import Header, Transaction, Footer
from library.operations import get_field, set_field, add_transaction
from library.questions import (
    get_validated_length,
    get_validated_amount,
    get_validated_currency
)
from library.locks import read_locks, add_lock, delete_lock
from library.constants import FIELD_LIST

from .helpers import read_data, locked
from .fullview import show_header, show_transactions, show_footer
from .ui import (
    print_general_menu,
    print_fields_menu,
    print_transaction_fields,
    print_banner,
    print_initial_menu,
    print_lock_menu,
    goodbye,
    WINDOW_WIDTH
)

def initial() -> None:
    """Display initial menu and handle the first user choice."""
    print_banner()
    time.sleep(0.5)
    print_initial_menu()
    while True:
        choice = input("Your choice: ").strip()
        if choice == "1":
            create_file_choice()
            choose_from_general()
            return
        elif choice == "2":
            choose_from_general()
            return
        elif choice == "3":
            goodbye()
            return
        else:
            print("Invalid option, please enter "
            "the number from 1 to 3")

def choose_from_general() -> bool | None:
    """Display the main menu and run selected one."""
    while True:
        print_general_menu()
        choice = input("Your choice: ").strip()
        if choice == "1":
            get_value_choice()
        elif choice == "2":
            change_value_choice()
        elif choice == "3":
            add_transaction_choice()
        elif choice == "4":
            get_data_choice()
        elif choice == "5":
            lock_field_choice()
        elif choice == "6":
            goodbye()
            return True
        else:
            print("Invalid option, please enter "
            "the number from 1 to 5")

def create_file_choice() -> None:
    """Generate a structured full file."""
    print("\nPreparation to generate a structured data file\n")

    blocked_fields = []
    for field in FIELD_LIST:
        if locked(field):
            blocked_fields.append(field)

    if blocked_fields:
        print("The following fields are locked:")
        for f in blocked_fields:
            print(f"- {f}")
        print("Unlock them first to continue.")
        return
    
    # Input header information.
    name = get_validated_length("Enter name: ", "name")
    surname = get_validated_length("Enter surname: ", "surname")
    patronymic = get_validated_length("Enter patronymic: ", "patronymic")
    address = get_validated_length("Enter address: ", "address")
    header = Header(name, surname, patronymic, address)

    # Input transactions.
    transactions = []
    while True:
        try:
            count = int(input("\nHow many transactions "
                        "do you want to add? "))
            if count <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter valid number.")

    for i in range(count):
        print(f"Transaction nr {i + 1}")
        amount = get_validated_amount("Enter amount: ")
        currency = get_validated_currency("Enter currency: ")
        
        transactions.append(
            Transaction(counter=str(i + 1),
            amount=amount,
            currency=currency)
        )

    # Calculate footer values.
    total_sum = 0
    for transaction in transactions:
        total_sum += transaction.amount
    
    footer = Footer(
        counter=len(transactions),
        sum=total_sum,
    )

    write_file("data.txt", header, transactions, footer)

def get_value_choice() -> None:
    """Read and display the selected field."""
    header, transactions, footer = read_data()
    
    while True:
        line = "-" * WINDOW_WIDTH
        title = "Select the field to read"
        print(f"\n{line}\n{title:^{WINDOW_WIDTH}}\n{line}")
        choice = print_fields_menu(True)

        if choice == "1":
            goal = get_field(
                header, transactions, footer,
                "header.name"
            )
            print(f"The name is {goal}.")
        elif choice == "2":
            goal = get_field(
                header, transactions, footer,
                "header.surname"
            )
            print(f"The surname is {goal}.")
        elif choice == "3":
            goal = get_field(
                header, transactions, footer,
                "header.patronymic"
            )
            print(f"The patronymic is {goal}.")
        elif choice == "4":
            goal = get_field(
                header, transactions, footer,
                "header.address"
            )
            print(f"The address is {goal}.")
        elif choice == "5":
            # Access one full transaction object.
            try:
                index = int(
                    input("Enter transaction counter from 1 to "
                          f"{len(transactions)}: ")
                )
                if not (1 <= index <= len(transactions)):
                    print("The counter is out of range.")
                    continue
                print("Select the field to read: ")
                print_transaction_fields(True)
                t_choice = input("Your choice: ").strip()
                if t_choice == "1":
                    goal = get_field(
                        header, transactions, footer,
                        f"transactions[{index}].counter"
                    )
                    print(f"The counter is {goal}.")
                elif t_choice == "2":
                    goal = get_field(
                        header, transactions, footer,
                        f"transactions[{index}].amount"
                    )
                    print(f"The amount is {goal}.")
                elif t_choice == "3":
                    goal = get_field(
                        header, transactions, footer,
                        f"transactions[{index}].currency"
                    )
                    print(f"The currency is {goal}.")
                else:
                    print("Invalid option.")
            except ValueError:
                print("Invalid option.")
        elif choice == "6":
            goal = get_field(
                header, transactions, footer,
                "footer.counter"
            )
            print(f"The total counter is {goal}.")
        elif choice == "7":
            goal = get_field(
                header, transactions, footer,
                "footer.sum"
            )
            print(f"The control sum is {goal}.")
        elif choice == "8":
            print(f"Going to the main menu.")
            break
        else:
            print("Invalid option, please enter "
            "the number from 1 to 8")

def change_value_choice() -> None:
    """Modify the selected field value and update the file."""
    header, transactions, footer = read_data()

    while True:
        line = "-" * WINDOW_WIDTH
        title = "Select the field to set"
        print(f"\n{line}\n{title:^{WINDOW_WIDTH}}\n{line}")
        choice = print_fields_menu(False)

        if choice == "1":
            if locked("header.name"):
                continue
            value = get_validated_length(
                "Enter new name: ",
                "name"
            )
            new_value = set_field(
                header, transactions, footer,
                "header.name", value
            )
            print(f"The name is now {new_value}.")
        elif choice == "2":
            if locked("header.surname"):
                continue
            value = get_validated_length(
                "Enter new surname: ",
                "surname"
            )
            new_value = set_field(
                header, transactions, footer,
                "header.surname", value
            )
            print(f"The surname is now {new_value}.")
        elif choice == "3":
            if locked("header.patronymic"):
                continue
            value = get_validated_length(
                "Enter new patronymic: ",
                "patronymic"
            )
            new_value = set_field(
                header, transactions, footer,
                "header.patronymic", value
            )
            print(f"The patronymic is now {new_value}.")
        elif choice == "4":
            if locked("header.address"):
                continue
            value = get_validated_length(
                "Enter new address: ",
                "address"
            )
            new_value = set_field(
                header, transactions, footer,
                "header.address", value
            )
            print(f"The address is now {new_value}.")
        elif choice == "5":
            try:
                index = int(input("Enter transaction counter from 1 to "
                                  f"{len(transactions)}: "))
                if not (1 <= index <= len(transactions)):
                    print("The counter is out of range.")
                    continue
                print("Select the field to read: ")
                print_transaction_fields(False)
                t_choice = input("Your choice: ").strip()
                if t_choice == "1":
                    if locked("transactions[*].amount"):
                        continue
                    value = get_validated_amount("Enter new amount: ")
                    new_value = set_field(
                        header, transactions, footer,
                        f"transactions[{index}].amount", value
                    )
                    print(f"The amount is now {new_value / 100.0}.")
                elif t_choice == "2":
                    if locked("transactions[*].currency"):
                        continue
                    value = get_validated_currency("Enter currency: ")
                    new_value = set_field(
                        header, transactions, footer,
                        f"transactions[{index}].currency", value
                    )
                    print(f"The new currency is {new_value}.")
                else:
                    print("Invalid option.")
            except ValueError:
                print("Invalid option.")
        elif choice == "6":
            print(f"Going to the main menu...")
            break
        else:
            print("Invalid option, please enter "
            "the number from 1 to 6")

def add_transaction_choice() -> None:
    """Append a new transaction record and update the file."""
    header, transactions, footer = read_data()

    if locked("transactions[*].amount") or locked("transactions[*].currency"):
        return

    print("\nAdding a new transaction\n")
    amount = get_validated_amount("Enter amount: ")
    currency = get_validated_currency("Enter currency: ")

    new_transaction = add_transaction(
        transactions, footer, header,
        amount, currency
    )
    print(f"Transaction nr {new_transaction.counter} was added")

def get_data_choice() -> None:
    """Display the full file content."""
    header, transactions, footer = read_data()
    
    show_header(header)
    show_transactions(transactions)
    show_footer(footer)

def lock_field_choice() -> None:
    while True:
        print_lock_menu()
        choice = input("Your choice: ").strip()

        if choice == "1":
            locks = read_locks()
            if not locks:
                print("There is no locked fields.")
            else:
                print("\nLocked fields:")
                for field in locks:
                    print(f"- {field}")

        elif choice == "2":
            print("\nLocking the field name.")
            print("List of possible strings to lock:")
            for i, field in enumerate(FIELD_LIST, start=1):
                print(f"  [{i}]  {field}")
            try:
                index = int(input("Enter number of the field: ").strip())
                if not (1 <= index <= len(FIELD_LIST)):
                    print("Incorrect number. Try again.")
                    continue
                field = FIELD_LIST[index -1]
                add_lock(field)
                print(f"{field} was locked successfiully.")
            except ValueError:
                print("Invalid option.")
        
        elif choice == "3":
            print("\nUnocking the field name.")
            locks = read_locks()
            if not locks:
                print("There are no fields to remove.")
                continue
            print("Select a field to unlock:")
            for i, field in enumerate(locks, start=1):
                print(f"  [{i}]  {field}")
            try:
                index = int(input("Enter number of the field: ").strip())
                if not (1 <= index <= len(locks)):
                    print("Incorrect number. Try again.")
                    continue
                field = locks[index -1]
                delete_lock(field)
                print(f"{field} was unlocked successfiully.")
            except ValueError:
                print("Invalid option.")

        elif choice == "4":
            print(f"Going to the main menu.")
            break
        else:
            print("Invalid option, please enter "
            "the number from 1 to 4")