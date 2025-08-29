class Inventory:
    """Simple inventory manager."""

    def __init__(self):
        self._items = {}

    def add_item(self, name: str, quantity: int = 1) -> None:
        if quantity < 0:
            raise ValueError("quantity must be non-negative")
        self._items[name] = self._items.get(name, 0) + quantity

    def remove_item(self, name: str, quantity: int = 1) -> None:
        if quantity < 0:
            raise ValueError("quantity must be non-negative")
        if name not in self._items:
            raise KeyError(name)
        if self._items[name] < quantity:
            raise ValueError("not enough quantity to remove")
        remaining = self._items[name] - quantity
        if remaining:
            self._items[name] = remaining
        else:
            del self._items[name]

    def get_quantity(self, name: str) -> int:
        return self._items.get(name, 0)

    def list_items(self) -> dict:
        return dict(self._items)
