## mBegin by reading in csv file

import csv

def init_clueset(cellchar):
    if (cellchar == ""):
        return full_clueset
    else:
        return {int(cellchar)}
### setup of variables

readin_state = {}

full_clueset = set(range(1, 10)) ###

f = open("puzzle1.csv")

rownames = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
for rowname in rownames:
    puzzle_row = f.readline()
    row_entries = puzzle_row.rstrip().split(",")

    for i in range(0, 9):
        cellname = rowname + str(i+1)
        entry = init_clueset(row_entries[i])
        readin_state[cellname] = {"Marked": "Unmarked", "Allowed":entry}

print(readin_state)


