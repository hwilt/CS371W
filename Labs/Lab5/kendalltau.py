def kendall_tau(rank1, rank2):
    """
    Compute the Kendall Tau distance between two rankings of the numbers
    from 0 to N-1

    Parameters
    ----------
    rank1: list
        A permutation of the elements 0, 1, ..., N-1
    rank2:
        A permutation of the elements 0, 1, ..., N-1
    
    Returns
    -------
    The Kendall-Tau distance, or the number of discordant pairs between
    the two rankings
    """
    n = len(rank1)
    discordant_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if rank1[i] > rank1[j] and rank2[i] > rank2[j]:
                discordant_pairs += 1
            elif rank1[i] < rank1[j] and rank2[i] < rank2[j]:
                discordant_pairs += 1
    return discordant_pairs

# This example should have 7 discordant pairs
rank1 = [0, 4, 3, 1, 2]
rank2 = [1, 4, 2, 3, 0]
print(kendall_tau(rank1, rank2))