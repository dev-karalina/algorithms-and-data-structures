from pathlib import Path
from .constants import LOCKS_PATH

def read_locks() -> list[str]:
    """Write locked field names in the file of locks."""
    if not Path(LOCKS_PATH).exists():
        return []
    try:
        locks = []
        with open(Path(LOCKS_PATH), 'r', encoding="UTF-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    locks.append(line)
        return locks
    except Exception:
        return []
    
def write_locks(locks: list[str]) -> None:
    """Save the list of locked fields to the file."""
    with open(Path(LOCKS_PATH), 'w', encoding="UTF-8") as file:
        for line in locks:
            file.write(line + "\n")

def is_locked(locks: list[str], field: str) -> bool:
    """Check if a field is locked."""
    if field in locks:
        return True
    
    if field.startswith("transactions["):
        content = field[len("transactions["):].split("].", 1)
        if len(content) == 2:
            index_str, field_name = content
            new_name = f"transactions[*].{field_name}"
            if new_name in locks:
                return True
            
    return False

def add_lock(field: str) -> None:
    """Add a lock for specific field."""
    locks = read_locks()
    if field not in locks:
        locks.append(field)
        write_locks(locks)

def delete_lock(field: str) -> None:
    """Remove a lock for specific field."""
    locks = read_locks()
    if field in locks:
        locks.remove(field)
        write_locks(locks)

def blocked(field: str) -> bool:
    locks = read_locks()
    if is_locked(locks, field):
        print("This field cannot be changed.")
        return True
    return False