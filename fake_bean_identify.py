#!/usr/bin/env python3
"""
Minimal stub for bean-identify.
Usage:  fake_bean_identify.py CONFIG IMPORT_DIR
It prints one ***** block per file found in IMPORT_DIR
plus a deterministic "Account:" line.

The real bean-identify command line utility, installed with beancount, identifies
all of the files in your import staging directory using your importers and 
prints the account details.
"""

import sys, pathlib, os

if len(sys.argv) != 3:
    sys.exit("usage: fake_bean_identify.py CONFIG IMPORT_DIR")

_, cfg, staging_dir = sys.argv
staging = pathlib.Path(staging_dir)

# Define specific mappings for each file
FILE_ACCOUNT_MAP = {
    "card.csv": "Liabilities:Credit-Card",
    "ss.pdf": "Income:Salary",
    "transactions.qfx": "Assets:Checking:Main"
}

for file in sorted(staging.glob("*")):
    if not file.is_file():
        continue
    
    file_name = os.path.basename(file)
    if file_name in FILE_ACCOUNT_MAP:
        print(f"**** {file}")
        print("Importer:    stub.importer")
        print(f"Account:     {FILE_ACCOUNT_MAP[file_name]}\n")
