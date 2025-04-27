from re import S
from persistence import *

import sys
import os

def add_branche(splittedline : list[str]):
    newBranche = Branche(splittedline[0], splittedline[1], splittedline[2])
    repo.branches.insert(newBranche)

def add_supplier(splittedline : list[str]):
    newSupplier = Supplier(splittedline[0], splittedline[1], splittedline[2])
    repo.suppliers.insert(newSupplier)

def add_product(splittedline : list[str]):
    newProduct = Product(splittedline[0], splittedline[1], splittedline[2], splittedline[3])
    repo.products.insert(newProduct)

def add_employee(splittedline : list[str]):
    newEmployee = Employee(splittedline[0], splittedline[1], splittedline[2], splittedline[3])
    repo.employees.insert(newEmployee)

adders = {  "B": add_branche,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}

def main(args : list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])

if __name__ == '__main__':
    main(sys.argv)