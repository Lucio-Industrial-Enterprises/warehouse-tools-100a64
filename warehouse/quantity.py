"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return a non-negative integer quantity, or raise ValueError."""
    quantity = int(value.strip())
    if quantity < 0:
        raise ValueError("quantity must be non-negative")
    return quantity
