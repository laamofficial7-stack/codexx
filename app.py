import argparse
import json
import os
from inventory import Inventory

DATA_FILE = "inventory_data.json"


def load_inventory() -> Inventory:
    inv = Inventory()
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            data = json.load(f)
        for name, qty in data.items():
            inv.add_item(name, qty)
    return inv


def save_inventory(inv: Inventory) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(inv.list_items(), f, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(description="Inventory manager")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="add an item")
    p_add.add_argument("name")
    p_add.add_argument("quantity", type=int)

    p_rm = sub.add_parser("remove", help="remove an item")
    p_rm.add_argument("name")
    p_rm.add_argument("quantity", type=int)

    sub.add_parser("list", help="list items")

    args = parser.parse_args()
    inv = load_inventory()

    if args.command == "add":
        inv.add_item(args.name, args.quantity)
    elif args.command == "remove":
        inv.remove_item(args.name, args.quantity)
    elif args.command == "list":
        for name, qty in inv.list_items().items():
            print(f"{name}: {qty}")

    save_inventory(inv)


if __name__ == "__main__":
    main()
