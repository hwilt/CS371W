def h(N):
    """
    A method to recursively compute how many moves
    there are in an optimal solution to the Towers of
    Hanoi problem

    Parameters
    ----------
    N: int
        Number of discs

    Returns
    -------
    Number of optimal moves needed to move discs
    """
    res = -1
    if N == 1:
        res = 1
    elif N > 1:
        ## TODO: Fill this in
        res = 2*h(N-1) + 1
    return res


for i in range(1, 10):
    print("{}.".format(h(i)), end='')