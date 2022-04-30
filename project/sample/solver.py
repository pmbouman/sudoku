import sys
import constants as c
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



def Nallowable(puzzle, cellname):
    """
    Input: uzzle value and name of cell
    Output: N of allowable values for that cell
    """
    return len(puzzle[cellname]["Allowable"])


""" TODO: Break function into two """


def inv_allowable_counts(puzzle):
    allowable_counts = {key: Nallowable(puzzle, key) for key in puzzle.keys()}

    inv_map = {}
    for key, value in allowable_counts.items():
        inv_map[value] = inv_map.get(value, []) + [key]

    return inv_map


def pull_unmarked(puzzle):
    return {k: v for k,  v in puzzle.items() if v["Marked?"] == "Unmarked"}


def min_number_allowable(inverted):
    return min(inverted.keys())


def neighbor_set(target_cell, neighborhood):
    match neighborhood:
        case "row":
            neighbor_set = [target_cell[0] + str(i) for i in range(1, 10)]
        case "col":
            neighbor_set = [rowname + target_cell[1] for rowname in c.ROWNAMES]
        case "subsquare":
            neighbor_set = subsq->cellnames[cellname->subsq[target_cell]]
###cSubsq -> cellnames is a dictionary mapping each subsquare to a list 
### of constitutive cell names
### cellname->subsquares is the inverse
### To add to constants.pyc code
        neighbor_set.remove(target_cell)
        return neighbor_set

def sweep_rows(puzzle, target_cell):
    ### revise to pass in rows, cols, or subsquare
    toreturn = {}

    target_value = puzzle[target_cell]["Allowable"]
    # Note thaat a singleton will still be a set of one"

    neighbor_set = neighbor_set_rows(target_cell)

    all_cell_names = puzzle.keys()
    for cellname in all_cell_names:
        cellval = puzzle[cellname]
        if (cellname in neighbor_set):
            fromset = puzzle[cellname]["Allowable"]
            fromset = fromset - target_value
            cellval["Allowable"] = fromset
        toreturn.update({cellname:  cellval})
    return toreturn
### Wow, this coud be a lot better

"""
def mainloop(puzzle):
    unmarked = pull_unmarked(puzzle)
    inverted_counts = inv_allowable_counts(unamrked)
    min_inverted_counts = min(inverted_counts.keys())
    cells_to_mark = len(unmarekd)

    if (cells_to_mark == 0):
        print_state(puzzle)
        return puzzle

    if min_inverted_acounts == 0 return puzzle 

    if min_inverted_accounts == 1:
        target_cell = inv_allowable_counts(puzzle)[1][0] 
        swept = sweepall(puzzle, target_cell))
        marked = markcells(swept, target_cell)
        return mainloop(marked)

    if min_inverted_accounts > 1:
        target_values = inverted_counts[min_inverted_counts][1]
        for value in target_values:


        ecurse on mainloop with the puzzle where the chosen cell has only
        one allowable value of the 2+ in that cell
"""
"""DEBUG"""
puzzle = i.readfile("/Users/peterbouman/Desktop/sudoku/project/data/puzzle1.csv")

