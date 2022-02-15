import numpy as np

def edit(s1, s2):
    """
    Parameters
    ----------
    s1: string of length M
        A string with M characters
    s2: string of length N
        A string with N characters
        
    Returns
    -------
    int: The optimal number of add/delete/match/swap
        operations needed to turn s1 into s2 or vice versa
    """
    M = len(s1)
    N = len(s2)
    table = np.zeros((M+1, N+1))
    # Fill in the base cases
    table[0, :] = np.arange(N+1)
    table[:, 0] = np.arange(M+1)
    for row in range(1, M+1):
        for col in range(1, N+1):
            cost1 = table[row, col-1] + 1
            cost2 = table[row-1, col] + 1 # Check table[i-1, j] + 1
            if s1[row-1] == s2[col-1]:
                cost3 = table[row-1, col-1]
            else:
                cost3 = table[row-1, col-1] + 1
            #cost3 = 0 # Check table[i-1, j-1] (+ 1 if s1[i-1] != s2[j-1])
            # Store table[i, j] as the min of the above possibilities
            table[row, col] = min(cost1, cost2, cost3)
    return int(table[M,N])

res = "{}.".format(edit("chris", "chase"))
res += "{}.".format(edit("school", "fools"))
res += "{}".format(edit("topology", "topography"))
print(res)