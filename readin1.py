## mBegin by reading in csv file

import csv

### setup of variables

readin_state = {}

full_clueset = set(range(1, 10)) ###

f = open("puzzle1.csv")

rownames = ["a", "b", "c", "d", "e", "f","g", "h", "i"]
for letter in rownames:
    print(letter)
    puzzle_row = f.readline()
    print(puzzle_row.rstrip().split(","))

def init_clueset(cellchar):
    if (cellchar == ""):
        return full_clueset
    else:
        return {int(cellchar)}

print(init_clueset("8"))
print(init_clueset(""))


