

def _clueset(cellchar):
    """
    Solver configured tp read from CSV with an entry
    for each cell (1:9) or a blank
    This creates the set of possible walues in puzzle.
    Allowable for that cell name.
    """
    full_allowable_set = set(range(1, 10))
    if (cellchar == ""):
        return full_allowable_set
    else:
        return {int(cellchar)}


""" TODO: break this into parts so that one fucntion reds the file and produces
a list of rows, for a second fuction to build the puzzle variable value """


def readfile(fname):
    readin_puzzle = {}
    f = open(fname)
    for rowname in ROWNAMES:
        puzzle_row = f.readline()
        row_entries = puzzle_row.rstrip().split(",")

        for i in range(1, 10):
            cellname = rowname + str(i)
            entry = init_allowable_set(row_entries[i-1])
            readin_puzzle[cellname] =\
                {"Marked?": "Unmarked", "Allowable": entry}
    f.close()
    return readin_puzzle


"""DEBUG"""
puzzle = readfile("/Users/peterbouman/Desktop/sudoku/project/data/puzzle1.csv")


def printcell(puzzle, cellname):
    allowables = puzzle[cellname]["Allowable"]
    if len(allowables) == 1:
        print(next(iter(allowables)), end="")
        """
        This construction extrcts the single elemnt of allowables
        in this branch
        """
    else:
        print(".", end="")


def print_state(puzzle):
    for rowname in ROWNAMES:
        for i in range(1, 10):
            printcell(puzzle, rowname + str(i))
            if i in {3, 6}:
                """ Using end = "" prints without newline"""
                print("|", end="")
        print("\n", end="")
        if rowname in {"c", "f"}:
            print("------------")
