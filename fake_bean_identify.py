#!/usr/bin/env python3
"""
Minimal stub for bean-identify.
Usage:  fake_bean_identify.py CONFIG IMPORT_DIR
It prints one ***** block per file found in IMPORT_DIR
plus a deterministic “Account:” line.

The real bean-identify command line utility, installed with beancount, identifies
all of the files in your import staging directory using your importers and 
prints the account details.
"""

import sys, pathlib, random

if len(sys.argv) != 3:
    sys.exit("usage: fake_bean_identify.py CONFIG IMPORT_DIR")

_, cfg, staging_dir = sys.argv
staging = pathlib.Path(staging_dir)

ACCOUNTS = [
    "Assets:Checking:Main",
    "Assets:Savings:Emergency",
    "Income:Salary",
    "Expenses:Food:Restaurants",
    "Expenses:Health:Pharmacy",
]

for file in sorted(staging.glob("*")):
    if not file.is_file():
        continue
    print(f"**** {file}")
    print("Importer:    stub.importer")
    print(f"Account:     {random.choice(ACCOUNTS)}\n")
