import sys
import pipes
import constants as c
import IO as i
"""
4/6/22 PMB
Solver is a sudoku solver that solves by depth-first
tree seaarch
Central data tructure is a dict mapping grid coordinates
(a1-b9") to two values: marked/unmarked (see below) and
the set of remaining allowable values for the cell 9which
will  be only one value for "solved" cells)

{ cellname _TO_ { Msrked? :  (Marked, Unmarked
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
    return c.invert_dict(allowable_counts)


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
            neighbor_set = c.SUBSQ_TO_CELLNAME[c.CELLNAME_TO_SUBSQ[target_cell]]
    neighbor_set.remove(target_cell)
    return neighbor_set



def sweepout(neighbor_set, puzzle, targetval):
    toreturn = puzzle
    for cellname in neighbor_set:
        fromset = toreturn[cellname]["Allowable"] - targetval
        print(fromset)
###        cellname["Allowable"] = fromset
###        toreturn.update({cellname:  cellval})
    return toreturn


def sweepall(target_cell, puzzle):
    targetval = puzzle[target_cell]["Allowable"]
    step1 = sweepout(neighbor_set(target_cell, "row"), puzzle, targetval)
    step2 = sweepout(neighbor_set(target_cell, "col"), step1, targetval)
    step3 = sweepout(neighbor_set(target_cell, "subsquare"), step2, targetval)
    return step3

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
puzzle = i.readfile("/home/peterbouman/Desktop/sudoku/project/data/puzzle1.csv")

