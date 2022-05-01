import itertools
"""and we setup the important constant for the list ["a" ... "i"]"""


def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


ROWNAMES = list(char_range("a", "i"))
ALLCELLS =  [(element[0] + str(element[1]))
    for element in itertools.product(ROWNAMES, list(range(1,10)))]

