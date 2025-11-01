from dataclasses import dataclass, field

@dataclass
class Header:
    """Store header information."""
    name: str
    surname: str
    patronymic: str
    address: str

@dataclass
class Transaction:
    """Store a single transaction record."""
    counter: str
    amount: float
    currency: str
    reserved: str = field(repr=False, default="")

@dataclass
class Footer:
    """Store footer information."""
    counter: int
    sum: float
    reserved: str = field(repr=False, default="")