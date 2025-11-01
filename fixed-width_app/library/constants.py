LINE_LEN = 120  # Total line length in the file.
T_MAX = 20_000  # Maximum number of transactions.

DATA_PATH = "data.txt"  # Path to the data structured file.
LOCKS_PATH = "data.locks.txt"  # Path to file with closed fields to changes.

# Identifiers of record types.
H_ID = "01"
T_ID = "02"
F_ID = "03"

# Header field positions.
H_NAME = (3, 30)
H_SURNAME = (31, 60)
H_PATRONYMIC = (61, 90)
H_ADDRESS = (91, 120)

# Transaction field positions.
T_COUNTER = (3, 8)
T_AMOUNT = (9, 20)
T_CURRENCY = (21, 23)
T_RESERVED = (24, 120)

# Footer field positions.
F_COUNTER = (3, 8)
F_SUM = (9, 20)
F_RESERVED = (21, 120)

# List of supperted currencies.
CURRENCIES = {
    "PLN",
    "USD",
    "EUR",
    "BYN",
    "UAH",
    "DKK",
    "NOK"
}

# Field name to position mapping.
FIELD_LIMITS = {
    "name": H_NAME,
    "surname": H_SURNAME,
    "patronymic": H_PATRONYMIC,
    "address": H_ADDRESS,
    "amount": T_AMOUNT,
}

# A list of fields that can be locked/unlocked
FIELD_LIST = [
    "header.name",
    "header.surname",
    "header.patronymic",
    "header.address",
    "transactions[*].amount",
    "transactions[*].currency",
]