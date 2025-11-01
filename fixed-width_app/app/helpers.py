from library.filehandler import read_file
from library.locks import is_locked, read_locks

def read_data() -> tuple | None:
    """Read 'data.txt' file and return structured data."""
    try:
        return read_file("data.txt")
    except Exception as e:
        print("Cannot read the file")
        return None, None, None
    
def locked(field: str) -> bool:
    """Return field is locked or not."""
    if is_locked(read_locks(), field):
        print("At least on of fields is locked "
        "and cannot be changed.")
        return True
    return False