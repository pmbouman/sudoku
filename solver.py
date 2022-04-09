import sys

"""
4/6/22 PMB
Solver is a sudoku solver that solves by depth-first
tree seaarch
Central data tructure is a dict mapping grid coordinates
(a1-b9") to two values: marked/unmarked (see below) and
the set of remaining allowable values for the cell 9which
will  be only one value for "solved" cells)

{ cellname -> { Msrked? :  (Marked, Unmarked
), Allowable: (set of allowable values remaining in cell)}}
Initialization means pluggig in values for cell "clues"
and then 1-9 for the blank cells
"""

""" First a utility function """
def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

"""and we setup the important constant for the list ["a" ... "i"]"""
ROWNAMES = list(char_range("a", "i"))


def init_clueset(cellchar):
    """
    Solver configured tp read from CSV with an entry
    for each cell (1:9) or a blank
    This creates the set of possible walues in puzzle.
    Allowed for that cell name.
    """
    FULL_CLUESET = set(range(1, 10))
    if (cellchar == ""):
        return FULL_CLUESET
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
            entry = init_clueset(row_entries[i-1])
            readin_puzzle[cellname] =\
                {"Marked?": "Unmarked", "Allowable": entry}
    f.close()
    return readin_puzzle


"""DEBUG"""
p1 = readfile("puzzle1.csv")


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


def Nallowed(puzzle, cellname):
    """
    Input: uzzle value and name of cell
    Output: N of allowable values for that cell
    """
    return len(puzzle[cellname]["Allowable"])


""" TODO: Break function into two """


def inv_allowed_counts(puzzle):
    allowed_counts = {key: Nallowed(puzzle, key) for key in puzzle.keys()}

    inv_map = {}
    for key, value in allowed_counts.items():
        inv_map[value] = inv_map.get(value, []) + [key]
 
    return inv_map


def pull_unmarked(puzzle):
    return {k: v for k,  v in puzzle.items() if v["Marked?"] == "Unmarked"}


def min_number_allowed(inverted):
    return min(inverted.keys())


def sweep_rows(puzzle, target_cell):
    toreturn = {}
    print(target_cell)

    target_value = list(puzzle[target_cell]["Allowable"])[0]
    print(target_value)

    cell_set = [target_cell[0] + str(i) for i in range(1, 10)]
    cell_set.remove(target_cell)

    for cellname in p1.keys():
        cellval = p1[cellname]
        if (cellname in cell_set):
            fromset = p1[cellname]["Allowed"]
            fromset = fromset - target_value
            cellval["Allowed"] = fromset
        print(cellname)
        print(cellval)
        toreturn.update({cellname:  cellval})
    return toreturn



"""
def mainloop(puzzle):
    unmarked = pull_unmarked(puzzle)
    inverted_counts = inv_allowed_counts(unamrked)
    min_inverted_counts = min(inverted_counts.keys())
    cells_to_mark = len(unmarekd)

    if (cells_to_mark == 0):
        print_state(puzzle)
        return puzzle

    if min_inverted_acounts == 0 return puzzle 

    if min_inverted_accounts == 1:
        target_cell = inv_allowed_counts(puzzle)[1][0] 
        swept = sweepall(puzzle, target_cell))
        marked = markcells(swept, target_cell)
        return mainloop(marked)

    if min_inverted_accounts > 1:
        target_values = inverted_counts[min_inverted_counts][1]
        for value in target_values:


        ecurse on mainloop with the puzzle where the chosen cell has only
        one allowable value of the 2+ in that cell
"""
