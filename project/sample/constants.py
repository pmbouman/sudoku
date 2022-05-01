import itertools
"""and we setup the important constant for the list ["a" ... "i"]"""


def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


ROWNAMES = list(char_range("a", "i"))
ALLCELLS =  [(element[0] + str(element[1]))
    for element in itertools.product(ROWNAMES, list(range(1,10)))]


LETTERS_SUMMAND = {"a":0, "b":0, "c":0, "d":3, "e":3, "f":3, "g":6, "h":6, "i":6}
NUMBERS_SUMMAND = {"1":0, "2":0, "3":0, "4":1, "5":1, "6":1, "7":2, "8":2, "9":2}

def get_subsq_number(cellname):
    return LETTERS_SUMMAND[cellname[0]] + NUMBERS_SUMMAND[cellname[1]]

CELLNAME_TO_SUBSQ = {k: get_subsq_number(k) for k in ALLCELLS}

def invert_dict(d):
    inv_map = {}
    for key, value in d.items():
        inv_map[value] = inv_map.get(value, []) + [key]

    return inv_map

SUBSQ_TO_CELLNAME = invert_dict(CELLNAME_TO_SUBSQ)

def sumsq_neighbors(cllname):
    return SUBSQ_TO_CELLNAME[CELLNAME_TO_SUBSQ[cellname]]
