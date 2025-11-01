import time

from .fullview import section

BANNER_TEXT = "Developed by Karalina Breiva"
WINDOW_WIDTH = 45
LINE = "-" * WINDOW_WIDTH

def print_banner(text: str = BANNER_TEXT) -> None:
    """Display the banner with author label."""
    frame = "-" * WINDOW_WIDTH
    middle = "|   " + f"\t{text}\t" + "    |"
    print(frame, middle, frame, sep='\n')

def print_initial_menu() -> None:
    """Display the initial menu options."""
    section("Choose an option")
    print("  [1]  Create new file")
    print("  [2]  Use existing file")
    print("  [3]  Exit")
    print(f"{LINE}")

def print_general_menu() -> None:
    """Display the general menu options."""
    section("Choose an option")
    print("  [1]  Get the value of the field")
    print("  [2]  Change the value of the field")
    print("  [3]  Add a new transaction")
    print("  [4]  Get the data of the file")
    print("  [5]  Lock actions")
    print("  [6]  Exit")
    print(f"{LINE}")

def print_fields_menu(footer_needed: bool) -> str:
    """Display the field selection options and return the choice."""
    if footer_needed:
        print("  [1]  Name")
        print("  [2]  Surname")
        print("  [3]  Patronymic")
        print("  [4]  Address")
        print("  [5]  Transaction field")
        print("  [6]  Total counter")
        print("  [7]  Control sum")
        print("  [8]  Back")
    else:
        print("  [1]  Name")
        print("  [2]  Surname")
        print("  [3]  Patronymic")
        print("  [4]  Address")
        print("  [5]  Transaction field")
        print("  [6]  Back")
        print("\nTotal counter, control sum and counter for")
        print("\ntransactions cannot be changed.")
        print("They are calculated automatically.")
        print("Thank you for understanding!")
    print(f"{LINE}")
    choice = input("Your choice: ").strip()
    return choice

def print_transaction_fields(counter_needed: bool) -> None:
    """Display the transaction selection options."""
    if counter_needed:
        print("  [1]  Counter")
        print("  [2]  Amount")
        print("  [3]  Currency")
    else:
        print("  [1]  Amount")
        print("  [2]  Currency")
    print(f"{LINE}")

def print_lock_menu() -> None:
    """Display the lock menu options."""
    section("Choose an option")
    print("  [1]  View locked fields")
    print("  [2]  Add a lock")
    print("  [3]  Remove a lock")
    print("  [4]  Back")
    print(f"{LINE}")

def goodbye() -> None:
    """Display exit messages."""
    print("\nThank you for using this app")
    time.sleep(1)
    print("Have a nice day!\nGoodbye!")
    time.sleep(1.5)