import numpy as np
import matplotlib.pyplot as plt
import json
from unionfind import *


class PhylogeneticNode:
    """
    A node in a phylogenetic tree
    """
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        self.parent = None
        self.inorder_pos = 0
        self.needleman_wunsch_score = 0

    def get_inorder(self, keys):
        if self.left:
            self.left.get_inorder(keys)
        self.inorder_pos = len(keys)
        if self.data:
            keys.append(self.data)
        else:
            keys.append("temp")
        if self.right:
            self.right.get_inorder(keys)

    def plot(self, width, depth):
        y = -depth
        x = self.inorder_pos
        # Draw a dot
        plt.scatter([x], [y], 50, 'k')
        # Draw some text indicating what the key is
        plt.text(x+width*0.05, y, "{}".format(self.data))
        # Offset in x
        dx = width/2**depth        
        if self.left:
            xnext = self.left.inorder_pos
            # Draw a line segment from my node to this left child
            plt.plot([x, xnext], [-depth, -depth-1])
            self.left.plot(width, depth+1)
        if self.right:
            xnext = self.right.inorder_pos
            # Draw a line segment from my node to this left child
            plt.plot([x, xnext], [-depth, -depth-1])
            self.right.plot(width, depth+1)

    
class Tree:
    """
    A phylogenetic tree
    """
    def __init__(self, nodes, edges, root):
        self.nodes = nodes
        self.edges = edges
        self.root = root

    def plot(self, width, animal_list):
        self.get_inorder()
        if self.root:
            self.root.plot(width, 0)
        plt.axis("off")
        plt.axis("equal")
        plt.show()

    def get_inorder(self):
        """
        Return the inorder traversal of the tree
        """
        keys = []
        if self.root:
            self.root.get_inorder(keys)
        return keys




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


def construct_dendrogram(species_data, animal_list):
    """
    Construct a dendrogram from species data
    1. Make a leaf node for each animal in the tree
    2. Sort the pairs of distances in decreasing order of Needleman-Wunsch similarity
    3. For each pair of animals in order of the above sort, check to see if they're part of the same connected component (using union find). If they are not, there's a new merge event. Create a new node in the tree with the root of each of their components as the two children (left/right is arbitrary here). Record the Needleman-Wunsch distance in that node.
    4. Once all of the animals are connected, set the root of the tree to be the last merged node.
    
    Parameters
    ----------
    Dictionary: Species_data
        key -> species and another species
        value -> distance between the two species

    Returns
    -------
    A instance of a Tree
        nodes and edges are filled in
    """
    # 1. Make a leaf node for each animal in the tree
    nodes = []
    for species in animal_list:
        nodes.append(PhylogeneticNode())
        nodes[-1].data = species

    #print([n.data for n in nodes])
    # 2. Sort the pairs of distances in decreasing order of Needleman-Wunsch similarity
    edges = []
    animalToNumber = [i for i in range(len(animal_list))]
    for i in range(len(animal_list)):
        for j in range(i+1, len(animal_list)):
            s1 = animal_list[i]
            s2 = animal_list[j]
            if s1 != s2:
                edges.append((i, j, species_data[animal_list[i] + "," + animal_list[j]]))
    
    #print(edges)
    # create a tree from bottom up (from leaves to root)
    # Sort the edges by distance
    edge = sorted(edges, key = lambda e: e[2])
    # Create a disjoint set
    djset = UnionFind(len(nodes))
    # Create a list of edges in the MST
    new_edges = []
    # Loop through the edges
    new_nodes = []
    for e in edge:
        (i, j, d) = e
        # If the two nodes are not in the same set, add the edge to the MST
        if not djset.find(i, j):
            djset.union(i, j)
            new_edges.append(e)
            new_nodes.append(PhylogeneticNode())
            new_nodes[-1].data = animal_list[i] + "," + animal_list[j]
            new_nodes[-1].left = nodes[i]
            new_nodes[-1].right = nodes[j]
            new_nodes[-1].needleman_wunsch_score = d
    root = new_nodes[-1]

    for n in new_nodes:
        if n.left:
            n.left.parent = n
        if n.right:
            n.right.parent = n

    #print([(n.data, n.left.data, n.right.data) for n in new_nodes])
    T = Tree(new_nodes, new_edges, root)
    return T
    

def needleman_wunsch_part1():
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

needleman_wunsch_part1()
species = json.load(open("organisms.json"))
species_data = json.load(open("distances.json"))
t = construct_dendrogram(species_data, list(species.keys()))
#print(t.edges)
#print(t.get_inorder())
t.plot(2, list(species.keys()))
