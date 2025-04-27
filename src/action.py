from persistence import *

import sys

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            if int(splittedline[1]) < 0:
                quantity = repo.products.find(id=splittedline[0])[0].quantity
                if quantity < (-1) * int(splittedline[1]):
                    continue
            if int(splittedline[1]) != 0:
                # update product quantity
                Product = repo.products.find(id = splittedline[0])
                Product[0].quantity += int(splittedline[1])
                repo.products.delete(id = splittedline[0])
                repo.products.insert(Product[0])
                # add activity
                newActivitie = Activitie(splittedline[0], splittedline[1], splittedline[2], splittedline[3])
                repo.activities.insert(newActivitie)


if __name__ == '__main__':
    main(sys.argv)