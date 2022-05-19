import copy
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

{ cellname : { Marked? :  ("Marked", "Unmarked"
), Allowable: (set of allowable values remaining in cell)}}
Initialization means pluggig in values for cell "clues"
and then 1-9 for the blank cells
"""

def Nallowable(puzzle, cellname):
    """
    Input: uzzle value and name of cell
    Output: integer N of allowable values for that cell
    """
    return len(puzzle[cellname]["Allowable"])


def inv_allowable_counts(puzzle):
    """
    Input: puzzle data structure
    Output: Inverted dictionary mapping number of allowable values to all the cellname
    """
    allowable_counts = {key: Nallowable(puzzle, key) for key in puzzle.keys()}
    return c.invert_dict(allowable_counts)


def pull_unmarked(puzzle):
    """
    Input: puzzle data structure
    Output: All cells from the puzzle not yet marked
    """
    return {k: v for k,  v in puzzle.items() if v["Marked?"] == "Unmarked"}


def pull_marked(puzzle):
    """
    Input: puzzle data structure
    Output: All cells from the puzzle already marked
    """
    return {k: v for k,  v in puzzle.items() if v["Marked?"] == "Marked"}



def min_number_allowable(inverted):
    """
    Input: inverted dictionary, mapping number sllowable to those cells
    Output: Integer, minimum number of alowable valuse in cells.
    If this is 0, there's an unfillable cell on the grid
    """
    return min(inverted.keys())


def neighbor_set(target_cell, neighborhood):
    """
    Input:  neighborhood is "row", "col" or "subsqaure"
          Target_cell is string, name of cell sweeping from (like "a3")
    Output: a *set* of cellnmes that are the indicated neighborhood
    for sweeping out values
    """
    match neighborhood:
        case "row":
            neighbor_set = set([target_cell[0] + str(i) for i in range(1, 10)])
        case "col":
            neighbor_set = set([rowname + target_cell[1] for rowname in c.ROWNAMES])
        case "subsquare":
            neighbor_set = set(c.SUBSQ_TO_CELLNAME[c.CELLNAME_TO_SUBSQ[target_cell]])
    neighbor_set.remove(target_cell)
    return neighbor_set


def sweepout(neighbor_set, puzzle, targetval):
    """
    Input: neighbor_set is the set of cellnames from 
    the neighbor_set function
    puzzle is a puzzle data sructure
    targetval is a one-element set to be sewpt out
    Output: puzzle structure with targetvsl swept out
    """
    toreturn = copy.deepcopy(puzzle)
    for cellname in neighbor_set:
        remaining_allowables = toreturn[cellname]["Allowable"] - targetval
        toreturn[cellname]["Allowable"] = remaining_allowables
    return toreturn


def sweepall(target_cell, puzzle):
    """
    Input: cellname (string) of target cell whose value  should be swept out
    output: puzzle data structure with target values swept out
    """
    targetval = puzzle[target_cell]["Allowable"] ### A one-element set
    step1 = sweepout(neighbor_set(target_cell, "row"), puzzle, targetval)
    step2 = sweepout(neighbor_set(target_cell, "col"), step1, targetval)
    step3 = sweepout(neighbor_set(target_cell, "subsquare"), step2, targetval)
    return step3

def markcells(puzzle, target_cell):
    toreturn = copy.deepcopy(puzzle)
    toreturn[target_cell]["Marked?"] = "Marked"
    return toreturn


def solver(puzzle):
    unmarked = pull_unmarked(puzzle)
    cells_to_mark = len(unmarked)

    if (cells_to_mark == 0):
        i.print_state(puzzle)
        return 1

    inverted_counts = inv_allowable_counts(unmarked)
    min_inverted_counts = min(inverted_counts.keys())

    if min_inverted_counts == 0:
        return 0

    if min_inverted_counts == 1:
        target_cell = inverted_counts[1][0]
        swept = sweepall(target_cell, puzzle)
        marked = markcells(swept, target_cell)
        return solver(marked)

    if min_inverted_counts > 1:
        unmarked = pull_unmarked(puzzle)
        inverted_counts = inv_allowable_counts(unmarked)
        min_inverted_counts = min(inverted_counts.keys())
        cells_to_mark = len(unmarked)
        target_cell = inverted_counts[min_inverted_counts][0]
        successes = 0
        for value in puzzle[target_cell]["Allowable"]:
            torecurse = copy.deepcopy(puzzle)
            torecurse[target_cell]["Allowable"] = {value}
            successes += solver(torecurse)
        if (successes > 0):
            return 1
        else:
            return 0
"""DEBUG"""
i.euler_doall("/Users/peterbouman/Desktop/sudoku/project/data/euler_sudoku.txt", solver)
