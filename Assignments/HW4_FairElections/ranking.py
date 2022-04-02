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


def get_pair_set(perm):
    pairs = set([])
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            pairs.add((perm[i], perm[j]))
    return pairs

def kendall_tau(p1, p2):
    """
    An O(n log n) algorithm for computing the Kendall-Tau Distance
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
    pairs1 = get_pair_set(p1)
    pairs2 = get_pair_set(p2)
    return len(pairs1-pairs2)


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
    return np.max(np.abs(D))


def get_average_ranking(animals, raters):
    """
    Compute the average ranking of each animal by each rater
    
    Parameters
    ----------
    animals: A list of animals in alphabetical order
    raters: dictionary( 
        string (Ranker's name): list (This person's permutation as a list of numbers
                                      corresponding to the indices in animals)

    Returns
    -------
    returns out the animals in the order of their average aggregated rankings
    example = [0,5,2,7,6,3,4,1]
    """
    N = len(animals)
    ret = [0]*N
    for rater in raters:
        for i, animal in enumerate(raters[rater]):
            ret[animal] += i
    for i in range(N):
        ret[i] /= len(raters)
    return np.argsort(ret)


def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp

def brute_force_kemeny_optimal(animals, raters, dictionary, idx = 0):
    """
    Compute the optimal permutation of animals using the Brute-Force algorithm using recursion
    Parameters
    ----------
    animals: A list of animals in alphabetical order
    raters: dictionary( 
        string (Ranker's name): list (This person's permutation as a list of numbers
                                      corresponding to the indices in animals)
    dict: dictionary( 
        int (idx): list
            A dictionary of permutations of animals
    idx: int
        The index of the current permutation
    
    Returns
    -------
    returns out the animals in the order of their average aggregated rankings
    example = [0,5,2,7,6,3,4,1]
    """
    if idx == len(animals) - 1:
        return dictionary
    for i in range(idx, len(animals)):
        swap(animals, i, idx)
        dictionary[idx] = animals.copy()
        brute_force_kemeny_optimal(animals, raters, dictionary, idx+1)
        swap(animals, i, idx-1)
    return dictionary


animals, raters = load_permutations()
#print(kendall_tau([0, 4, 3, 1, 2], [1, 4, 2, 3, 0]))
#plt.figure(figsize=(8,8))
#plot_mds_distances(raters, 1)
#plt.show()

print("Part 2:\n",diameter(raters))

rank = get_average_ranking(animals, raters)
print("Part 3:\n", rank)
i = 1
for r in rank:
    print(i, animals[r])
    i += 1

brute_rank = brute_force_kemeny_optimal(animals, raters, {})
print("\nPart 4:\n", brute_rank)
i = 1
for r in brute_rank:
    print(i, animals[r])
    i += 1