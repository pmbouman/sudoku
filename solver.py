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


ROWNAMES = list(char_range("a ", "i"))

def Unmarked_only(puzzle):
    return dict(filter(lambda elem: elem[1]["Marked?"] == "Unmarked", puzzle.items()))


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
    ROWNAMES = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    for rowname in ROWNAMES:
        for i in range(1, 10):
            printcell(puzzle, rowname + str(i))
            if i in {3, 6}:
                print("|", end="")
        print("\n", end="")
        if rowname in {"c", "f"}:
            print("------------")


def Nallowed(puzzle, cellname):
    return len(puzzle[cellname]["Allowed"])


def inv_allowed_counts(puzzle):
    counts = dict(map(lambda cellname: Nallowed(puzzle, cellname), puzzle.keys()))

    inv_map = {}
    for key, value in counts.items():
        inv_map[value] = inv_map.get(value, []) + [key]
 
    return inv_map

"""


main loop

min_number_allowed(cell_list):
    Pull sizes of all allowed sets on cell_list
    Return minimum of this list

def minloop(puzzle):
inv_map = {}
for k, v in my_map.iteritems():
    inv_map[v] = inv_map.get(v, []) + [k]




def mainloop(puzzle):
     Make a local mutable copy of puzzle parameter

    select all the unmarked 'cells' from puzzle
    the result will be a sub-dictionary
     If zero unmarked cells: print_state, return 1 - another solution
         Find a cell with the smallest allowable size

    if min_number_allowed(unmarked_cells) == 0, halt and return Nsol

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
