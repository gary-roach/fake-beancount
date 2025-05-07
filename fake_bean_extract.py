#!/usr/bin/env python3
"""
Minimal stub for bean-extract.
Usage:  fake_bean_extract.py  -f LEDGER CONFIG FILE
Ignores LEDGER/CONFIG and prints 3 fake transactions for FILE.

The real bean-identify command line utility, installed with beancount, extracts
transactions from your institution statements/exports and outputs formated 
beancount transactions
"""

import sys, pathlib, random, datetime as dt

if len(sys.argv) < 5 or sys.argv[1] != "-f":
    sys.exit("usage: fake_bean_extract.py -f LEDGER CONFIG FILE")

file_path = pathlib.Path(sys.argv[4])
base_name = file_path.stem.capitalize()

accounts = [
    "Assets:Checking:Main",
    "Assets:Savings:Emergency",
    "Expenses:Food:Restaurants",
    "Expenses:Health:Pharmacy",
]

today = dt.date.today()

def txn(i: int) -> str:
    date = today - dt.timedelta(days=i)
    payee  = f"{base_name} Payee {i}"
    narr   = f"Sample transaction {i}"
    acct1  = random.choice(accounts)
    acct2  = random.choice([a for a in accounts if a != acct1])
    amt    = round(random.uniform(10, 120), 2)
    return (
        f"{date} * \"{payee}\" \"{narr}\"\n"
        f"  {acct1}     {amt} USD\n"
        f"  {acct2}    -{amt} USD\n"
        "\n"
    )

print("".join(txn(i) for i in range(1, 4)))
