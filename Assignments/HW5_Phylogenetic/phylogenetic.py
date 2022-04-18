import numpy as np
import matplotlib.pyplot as plt
import json
from unionfind import *
from Trees import *

def load_blosum(filename):
    """
    Load in a BLOSUM scoring matrix for Needleman-Wunsch

    Parameters
    ----------
    filename: string
        Path to BLOSUM file
    
    Returns
    -------
    A dictionary of {string: int}
        Key is string, value is score for that particular 
        matching/substitution/deletion
    """
    fin = open(filename)
    lines = [l for l in fin.readlines() if l[0] != "#"]
    fin.close()
    symbols = lines[0].split()
    X = [[int(x) for x in l.split()] for l in lines[1::]]
    X = np.array(X, dtype=int)
    N = X.shape[0]
    costs = {}
    for i in range(N-1):
        for j in range(i, N):
            c = X[i, j]
            if j == N-1:
                costs[symbols[i]] = c
            else:
                costs[symbols[i]+symbols[j]] = c
                costs[symbols[j]+symbols[i]] = c
    return costs


def needleman_wunsch(s1, s2, _dict):
    """
    Perform Needleman-Wunsch alignment on two strings

    Parameters
    ----------
    s1: string
        First string
    s2: string
        Second string
    _dict: dictionary
        Dictionary of {string: int}
        Key is string, value is score for that particular 
        matching/substitution/deletion

    Returns
    -------
    A tuple of (int)
        The first element is the score of the alignment
    """
    N = len(s1)
    M = len(s2)
    # Initialize the scoring matrix
    S = np.zeros((N+1, M+1))
    # Fill in the first row and column
    for i in range(1, N+1):
        S[i, 0] = S[i-1, 0] + _dict[s1[i-1]]
    for j in range(1, M+1):
        S[0, j] = S[0, j-1] + _dict[s2[j-1]]
    # Fill in the rest of the matrix
    for i in range(1, N+1):
        for j in range(1, M+1):
            match = S[i-1, j-1] + _dict[s1[i-1]+s2[j-1]]
            del1 = S[i-1, j] + _dict[s1[i-1]]
            del2 = S[i, j-1] + _dict[s2[j-1]]
            # Choose the best score
            S[i, j] = max(match, del1, del2)
    return S[N, M]


def construct_dendrogram():
    pass


costs = {"a":-1, "b":-2, "ab":-3, "ba":-3, "aa":2, "bb":3}
s1 = "aabaab"
s2 = "ababaa"
print("aabaab & ababaa = " + str(needleman_wunsch(s1, s2, costs)))

costs = load_blosum("blosum62.bla")
species = json.load(open("organisms.json"))
s1 = "Dog"
s2 = "Hyaena"
sp1 = species[s1]
sp2 = species[s2]
print("Dog & Hyaena = " + str(needleman_wunsch(sp1, sp2, costs)))

s1 = "Domestic Cat"
s2 = "Cougar"
sp1 = species[s1]
sp2 = species[s2]
print("Domestic Cat & Cougar = " + str(needleman_wunsch(sp1, sp2, costs)))
'''
x = {("Dog,Dingo"):1337, ("Dingo,Dog"):1337}
json.dump(x, open("similarities.json", "w"))

# go through each pair of species
data = {}
animals = list(species.keys())
for i in range(len(animals)):
    for j in range(i+1, len(animals)):
        s1 = species[animals[i]]
        s2 = species[animals[j]]
        data[animals[i]+","+animals[j]] = needleman_wunsch(s1, s2, costs)
print(data)
json.dump(data, open("distances.json", "w"))
'''
species_data = json.load(open("distances.json"))

