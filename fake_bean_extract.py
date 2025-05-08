#!/usr/bin/env python3
"""
Minimal stub for bean-extract.
Usage:  fake_bean_extract.py  -f LEDGER CONFIG FILE
Outputs file-specific transactions based on the file type.

The real bean-extract command line utility, installed with beancount, extracts
transactions from your institution statements/exports and outputs formatted 
beancount transactions
"""

import sys, pathlib, random, datetime as dt
import os

if len(sys.argv) < 5 or sys.argv[1] != "-f":
    sys.exit("usage: fake_bean_extract.py -f LEDGER CONFIG FILE")

path_arg = pathlib.Path(sys.argv[4])

# Use May 2025 as our reference date for consistent output
today = dt.date(2025, 5, 8)

def process_file(file_path):
    """Process a single file and output transactions for it."""
    base_name = os.path.basename(file_path).lower()
    
    # Print the file path header like the real bean-extract would
    print(f"**** {file_path.absolute()}\n")

    # Generate different transactions based on the file type
    if base_name == "card.csv":
        # Credit card transactions
        date1 = dt.date(2025, 5, 5)
        date2 = dt.date(2025, 5, 3)
        date3 = dt.date(2025, 4, 28)
        
        print(f"{date1} * \"Restaurant\" \"Dinner\"")
        print(f"  Expenses:Food:Restaurants     78.45 USD")
        print(f"  Liabilities:Credit-Card      -78.45 USD")
        print("")
        
        print(f"{date2} * \"Gas Station\" \"Fuel\"")
        print(f"  Expenses:Transport:Fuel       45.32 USD")
        print(f"  Liabilities:Credit-Card      -45.32 USD")
        print("")
        
        print(f"{date3} * \"Online Store\" \"Electronics\"")
        print(f"  Expenses:Shopping:Electronics  129.99 USD")
        print(f"  Liabilities:Credit-Card      -129.99 USD")
        print("")
        
    elif base_name == "ss.pdf":
        # Salary/paycheck - similar to the example provided
        date = dt.date(2025, 4, 25)
        
        print(f"{date} * \"Paycheck\"")
        print(f"  Assets:Zero-Sum-Accounts:Transfers       10000.00 USD")
        print(f"  Expenses:Taxes                           -2000.00 USD")
        print(f"  Income:Salary                            -8000.00 USD")
        print("")
        
    elif base_name == "transactions.qfx":
        # Bank account transactions with interest and balance assertion
        date1 = dt.date(2025, 4, 30)
        balance_date = dt.date(2025, 5, 7)
        
        print(f"{date1} * \"Interest Earned\" \"INTEREST CREDIT\"")
        print(f"  Assets:Checking:Main    62.59 USD")
        print(f"  Income:Interest:Checking:Main")
        print("")
        
        # Balance assertion
        print(f"{balance_date} balance Assets:Checking:Main    18137.95 USD")
        print("")

    else:
        # For any other file types - fallback to generic transactions
        def txn(i: int) -> str:
            date = today - dt.timedelta(days=i)
            payee = f"{file_path.stem.capitalize()} Payee {i}"
            narr = f"Sample transaction {i}"
            acct1 = "Expenses:Miscellaneous"
            acct2 = "Assets:Checking:Main"
            amt = round(random.uniform(10, 120), 2)
            return (
                f"{date} * \"{payee}\" \"{narr}\"\n"
                f"  {acct1}     {amt} USD\n"
                f"  {acct2}    -{amt} USD\n"
                "\n"
            )
        
        print("".join(txn(i) for i in range(1, 4)))

# Check if the path is a directory or a file
if path_arg.is_dir():
    # Process all files in the directory
    for file_path in sorted(path_arg.glob("*")):
        if file_path.is_file():
            process_file(file_path)
else:
    # Process a single file
    process_file(path_arg)
