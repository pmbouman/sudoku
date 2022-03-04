def marked_only(puzzle):
    return dict(filter(lambda elem: elem[1]["Marked"] == "Marked", puzzle.items()))


def init_clueset(cellchar):
    FULL_CLUESET = set(range(1, 10))
    if (cellchar == ""):
        return FULL_CLUESET
    else:
        return {int(cellchar)}


def readfile(fname):
    ROWNAMES = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    readin_state = {}
    f = open(fname)
    for rowname in ROWNAMES:
        puzzle_row = f.readline()
        row_entries = puzzle_row.rstrip().split(",")

        for i in range(1, 10):
            cellname = rowname + str(i)
            entry = init_clueset(row_entries[i-1])
            """ column name are 1-based,
            row_entry elements are 0-based"""

            readin_state[cellname] = {"Marked": "Unmarked", "Allowed": entry}
    f.close()
    return readin_state


def printcell(puzzle, cellname):
    allowables = puzzle[cellname]["Allowed"]
    if len(allowables) == 1:
        print(next(iter(allowables)), end="")
        """ NOTE: learn why next(iter(set)) works """
    else:
        print(".", end="")
        """NOTE:  add code to make spaces between subsquares """


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

""" Pseudocode for the main loop 

min_number_allowed(cell_list):
    Pull sizes of all allowed sets on cell_list
    Return minimum of this list



def mainloop(puzzle, Nsol):
     Make a local mutable copy of puzzle parameter
     Nsol is the number of solutions so far
    invoke as  mainloop(readin_state, 0)

    select all the unmarked 'cells' from puzzle
    the result will be a sub-dictionary
     If zero unmarked cells: print_state, return Nsol+1 - another solution  
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
