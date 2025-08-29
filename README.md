# Inventory Software

This project provides a minimal inventory manager with a command line
interface and a small Python API.

## Command line usage

```
python app.py add apple 10
python app.py remove apple 3
python app.py list
```

Inventory data is stored in a JSON file named `inventory_data.json` in the
current directory. The `list` command prints all items and their quantities:

```
python app.py list
#> apple: 7
```

## Python API

```
from inventory import Inventory

inv = Inventory()
inv.add_item("apple", 5)
```
