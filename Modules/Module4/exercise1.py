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
    
    res = 0
    # Stopping conditions
    if len(s1) == 0:
        res = len(s2)
    elif len(s2) == 0:
        res = len(s1)
    else:
        # Delete last character from s1 and match the rest recursively
        case1 = 1 + edit(s1[0:-1], s2) 
        ## TODO: Fill in the other two cases 
        # Delete last character from s2 and match the rest recursively
        case2 = 1 + edit(s1, s2[0:-1])
        # Swap or match the last characters from s1 and s2 and match the rest recursively
        if s1[-1] == s2[-1]:
            case3 = edit(s1[0:-1], s2[0:-1])
        else:
            case3 = 1 + edit(s1[0:-1], s2[0:-1])
        #case3 = edit(s1[0:-1], s2[0:-1])
        res = min(case1, case2, case3)
    return res

res = "{}.".format(edit("chris", "chase"))
res += "{}.".format(edit("school", "fools"))
res += "{}".format(edit("topology", "topography"))
print(res)