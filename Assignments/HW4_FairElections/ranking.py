import time
import numpy as np
import matplotlib.pyplot as plt


def load_permutations(filename="preferences.csv"):
    """
    Load all student permutations from a file

    Parameters
    ----------
    filename: string
        Path to a file
    
    Returns
    -------
    animals: A list of animals in alphabetical order
    raters: dictionary( 
        string (Ranker's name): list (This person's permutation as a list of numbers
                                      corresponding to the indices in animals)
    )
    """
    raters = {}
    fin = open(filename)
    lines = fin.readlines()
    fin.close()
    animals = [s.rstrip().replace("\"", "") for s in lines[0].split(",")[1::]]
    for line in lines[1::]:
        fields = line.split(",")
        rater = fields[0].replace("\"", "")
        fields = [int(f) for f in fields[1::]]
        raters[rater] = [0]*len(fields)
        for i, x in enumerate(fields):
            raters[rater][x-1] = i
    return animals, raters


def mds(D):
    """
    Perform classic multidimensional scaling
    See notes here:
    http://www.cs.umd.edu/~djacobs/CMSC828/MDSexplain.pdf

    Parameters
    ----------
    D: ndarray(N, N)
        A matrix of pairwise similarities
    
    Return
    ------
    Y: ndarray(N, N)
        MDS projection, with columns in order of variance
        explained
    """
    from numpy import linalg
    N = D.shape[0]
    H = np.eye(N) - np.ones((N, N))/N
    B = -0.5*(H.dot((D*D).dot(H)))
    U, s, V = linalg.svd(B)
    Y = np.sqrt(s[None, :])*U
    return Y

def plot_mds_distances(raters, random_state=0):
    """
    Compute all pairwise Kendall-Tau distances and plot a dimension 
    reduction from the Kendall-Tau metric space to 2D to visualize how
    similar different raters are

    Parameters
    ----------
    raters: dictionary( 
        string (Ranker's name): list (This person's permutation as a list of numbers
                                      corresponding to the indices in animals)
    random_state: int
        A seed to determine which random isometry to use for MDS
    """
    N = len(raters)
    D = np.zeros((N, N))
    rlist = [r for r in raters]
    for i, rater1 in enumerate(rlist):
        for j in range(i+1, N):
            rater2 = rlist[j]
            D[i, j] = kendall_tau(raters[rater1], raters[rater2])
    D = D+D.T
    X = mds(D)
    plt.scatter(X[:, 0], X[:, 1])
    for i, r in enumerate(rlist):
        plt.text(X[i, 0], X[i, 1], r)
    plt.title("MDS Projected Kendall-Tau Distances")


def kendall_tau(p1, p2):
    """
    An O(N log N) algorithm for computing the Kendall-Tau Distance

    Parameters
    ----------
    p1: List of N elements
        A permutation of the elements 0, 1, 2, ..., N corresponding 
        to the first rating
    p2: List of N elements
        A permutation of the elements 0, 1, 2, .., N corresponding to 
        the second rating
    
    Returns
    -------
    The Kendall-Tau distance between permutation p1 and p2
    """
    n = len(p1)
    discordant_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if p1[i] > p1[j] and p2[i] > p2[j]:
                discordant_pairs += 1
            elif p1[i] < p1[j] and p2[i] < p2[j]:
                discordant_pairs += 1
    return discordant_pairs


def diameter(raters):
    """
    Compute the diameter of the raters graph

    Parameters
    ----------
    raters: dictionary( 
        string (Ranker's name): list (This person's permutation as a list of numbers
                                      corresponding to the indices in animals)
    """
    ret = []
    N = len(raters)
    D = np.zeros((N, N))
    rlist = [r for r in raters]
    for i, rater1 in enumerate(rlist):
        for j in range(i+1, N):
            rater2 = rlist[j]
            D[i, j] = kendall_tau(raters[rater1], raters[rater2])

    D = D+D.T
    print(np.max(D))
    return ret


#print(kendall_tau([0, 4, 3, 1, 2], [1, 4, 2, 3, 0]))
plt.figure(figsize=(8,8))
animals, raters = load_permutations()
#plot_mds_distances(raters, 1)
#plt.show()
print(diameter(raters))