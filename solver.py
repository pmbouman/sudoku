 import sys
"""

Celtral data tructure is a dict mapping grid coordinates
(a1-b9") to two values: marked/unmarked (see below) and
the set of remaining allowable values for the cell 9which
may be only one value for "solved" cells)

Initialization means pluggig in values for cell "clues"
and then 1-9 for the blank cells
"""


def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


ROWNAMES = list(char_range("a", "i"))


def Unmarked_only(puzzle):
    return dict(filter(lambda elem: elem[1]["Marked?"] == "Unmarked",
                       puzzle.items()))


def init_clueset(cellchar):
    """
    During readin, the argument is the character from that cell
    in the input file: either "", meaning ni vskue yet,
    or the cell has a clue, and  return a size 1 set of 
    the starting value of that cell
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
            readin_puzzle[cellname] = {"Marked?": "Unmarked", "Allowed": entry}
    f.close()
    return readin_puzzle


"""DEBUG"""
p1 = readfile("puzzle1.csv")


def printcell(puzzle, cellname):
    allowables = puzzle[cellname]["Allowed"]
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
    return len(puzzle[cellname]["Allowed"])


""" TODO: Break function into two """


def inv_allowed_counts(puzzle):
    allowed_counts = {key: Nallowed(puzzle, key) for key in puzzle.keys()}

    inv_map = {}
    for key, value in allowed_counts.items():
        inv_map[value] = inv_map.get(value, []) + [key]
 
    return inv_map


def pull_unmarked(puzzle):
    return {k: v for k,  v in puzzle.items() if v["Marked?"] == "Unmarked"}

 
"""
def mainloop(puzzle):
    unmarked = pull_unmarked(puzzle)
    if (len(unmarked)) == 0:
        print_state(puzzle)
        sys.exit("Solution found")

    if min_number_allowed(unmarked) == 0:
        sys.exit("no solution found")

    else if (min_number_alloed
         Else if minsize is 1, sweep value from rows, columns
         and subsquares in the total puzzle copy
         (not just the unmarked cells)
         NOTE: subsquare attribute must be added to puzzle data structure
         Mark the square in the whole puzzle
    Then repeat at line 59

        Else if smallest allowed set is size 2+:
        Choose a cell of that size
        for each allowable value in the cell,
        recurse on mainloop with the puzzle where the chosen cell has only
        one allowable value of the 2+ in that cell
        Use Nsol output from last call as parameter for each of these calls
        Return the updated Nsol as end of function
"""
