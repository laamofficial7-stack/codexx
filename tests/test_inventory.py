import sys
import os
import pytest

# Ensure root path is in sys.path to import inventory package
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from inventory import Inventory


def test_add_and_get_quantity():
    inv = Inventory()
    inv.add_item("apple", 5)
    assert inv.get_quantity("apple") == 5


def test_remove_item():
    inv = Inventory()
    inv.add_item("banana", 3)
    inv.remove_item("banana", 2)
    assert inv.get_quantity("banana") == 1
    inv.remove_item("banana", 1)
    assert inv.get_quantity("banana") == 0


def test_remove_missing_raises():
    inv = Inventory()
    with pytest.raises(KeyError):
        inv.remove_item("missing")


def test_list_items_returns_copy():
    inv = Inventory()
    inv.add_item("carrot", 2)
    items = inv.list_items()
    items["carrot"] = 100
    assert inv.get_quantity("carrot") == 2
