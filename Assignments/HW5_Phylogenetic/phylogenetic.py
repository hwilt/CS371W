import numpy as np
import matplotlib.pyplot as plt
import json
from unionfind import *


class PhylogeneticNode:
    """
    A node in a phylogenetic tree
    """
    def __init__(self, param):
        self.sim = 0
        self.key = None
        if type(param) is str:
            self.key = param
        else:
            self.sim = param
        self.left = None
        self.right = None

    def __str__(self):
        """
        String is key if key is not None, or blank otherwise
        """
        ret = ""
        if self.key:
            ret = "{}".format(self.key)
        return ret

    def compute_y_coords(self, maxsim=[0], y=[0]):
        """
        Recursively compute y coordinate of nodes via an inorder
        traversal, while computing the maximum phylogenetic 
        similarity as a side effect

        Parameters
        ----------
        maxsim: list of [int]
            Maximum similarity
        y: list of [int]
            Current y coordinate
        """
        if self.left:
            self.left.compute_y_coords(maxsim, y)
        maxsim[0] = max(maxsim[0], self.sim)
        self.y = y[0]
        y[0] += 1
        if self.right:
            self.right.compute_y_coords(maxsim, y)

    def compute_x_coords(self, maxsim):
        """
        Recursively compute and store the x coordinates
        of all nodes.  If the nodes are internal, then the
        x coordinate is the phylogenetic similarity.
        If the node is a leaf node, then the x coordinate
        is the maximum phylogenetic similarity among all
        internal nodes

        Parameters
        ----------
        maxsim: int
            Maximum phylogenetic similarity across all nodes
        """
        if self.left:
            self.left.compute_x_coords(maxsim)
        if self.right:
            self.right.compute_x_coords(maxsim)
        if self.key:
            self.x = maxsim
        else:
            self.x = self.sim
            
    def draw(self):
        """
        Recursively draw phylogenetic tree.  Assumes that the
        x and y coordinates have been precomputed
        """
        x1, y1 = self.x, self.y
        # Draw a dot
        plt.scatter(x1, y1, 50, 'k')
        # Draw some text indicating what the key is
        plt.text(x1+10, y1, "{}".format(self))
        if self.left:
            # Draw a line segment from my node to this left child
            x2, y2 = self.left.x, self.left.y
            plt.plot([x1, x2], [y1, y2])
            self.left.draw()
        if self.right:
            # Draw a line segment from my node to this right child
            x2, y2 = self.right.x, self.right.y
            plt.plot([x1, x2], [y1, y2])
            self.right.draw()

    
class Tree:
    """
    A phylogenetic tree
    """
    def __init__(self):
        self.root = None

    def draw(self, threshold=None):
        """
        Draw the phylogenetic tree from the bottom up

        Parameters
        ----------
        threshold: int
            If specified, draw a vertical line showing a similarity
            threshold for clustering
        """
        if self.root:
            maxsim = [0]
            self.root.compute_y_coords(maxsim)
            self.root.compute_x_coords(maxsim[0])
            self.root.draw()
            ax = plt.gca()
            xlim = ax.get_xlim()
            ax.set_xlim([xlim[0], xlim[1]+200])
            if threshold:
                ylim = ax.get_ylim()
                plt.plot([threshold, threshold], [ylim[0], ylim[1]], 'k', linestyle='--', linewidth=3)
                plt.title("Similarity Threshold = {}".format(threshold))
            ax.set_yticks([])
            plt.xlabel("Needleman-Wunsch Similarity")
            plt.tight_layout()
            plt.show()

    def start_cluster_rec(self, thresh):
        """
        Method that starts the recursion for putting nodes in clusters

        Parameters
        ----------
        thresh : int
            Threshold for clustering 

        Returns
        -------
        clusters : list
            list of lists containing clusters of species

        """
        clusters = list()
        node = self.root
        self.kruskal_cluster(node, thresh, clusters)
        print(clusters)
        return clusters
    
    def kruskal_cluster(self, node, thresh, clusters):
        """
        Creates clusters based on if a species is greater than a given threshold

        Parameters
        ----------
        node : TreeNode
            Current species being evaluated
        thresh : int
            Threshold for clustering
        clusters : list
            List of lists containing clusters of species

        """
        if node.key:
            keyList = [node.key]
            clusters.append(keyList)  
        elif node.sim >= thresh:
            descendants = list()
            self.enumerate_descendants(node, descendants)
            clusters.append(descendants)
        else:
            if node.right:
                self.kruskal_cluster(node.right, thresh, clusters)
            if node.left:
                self.kruskal_cluster(node.left, thresh, clusters)
                
    def enumerate_descendants(self, node, descendants):
        """
        Enumerates a list of all the descendents of a given species

        Parameters
        ----------
        node : TreeNode
            The name of a species
        descendants : List
            List containing all descendents of a given species

        """
        if node.key:
            descendants.append(node.key)
        if node.left:
            self.enumerate_descendants(node.left, descendants)
        if node.right:
            self.enumerate_descendants(node.right, descendants)




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


def construct_dendrogram(species):
    """
    Construct a dendrogram from species data
    
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

    species_list = list()
    for s in species.keys():
        species_list.append(PhylogeneticNode(s))   
    
    djset = UnionFind(len(species_list))
    
    
    roots = list()
    for node in species_list:
        roots.append(node)
    
    
    keys = dict()
    for i, s in enumerate(list(species.keys())):
        keys[s] = i
    
    #print(species_data)
    #all_pairs = json.load(open("distances.json"))
    all_pairs = json.load(open("distances.json"))["all_pairs"]
    all_pairs = sorted(all_pairs.items(), key = lambda info: info[1], reverse=True)
    #print(all_pairs)
    for pair in all_pairs:
        #print(pair)
        current_pair = pair[0].split('_')
        #print(current_pair)
        for i in range(len(current_pair)-1):
            species1 = current_pair[i]
            species2 = current_pair[i+1]
            #print(species1, species2)
            s1_index = keys[species1]
            s2_index = keys[species2]
            s1_root = djset.root(s1_index)
            s2_root = djset.root(s2_index)
            if s1_root != s2_root:
                #print(pair[1])
                new_node = PhylogeneticNode(pair[1])
                new_node.left = roots[s1_root]
                new_node.right = roots[s2_root]
                djset.union(s1_root, s2_root)
                roots[s1_root] = new_node
                roots[s2_root] = new_node
    #print([n for n in new_nodes])
    T = Tree()
    T.root = new_node
    print(T.root)
    plt.figure(figsize=(10, 14))
    T.draw()
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

def main():
    needleman_wunsch_part1()
    species = json.load(open("organisms.json"))

    t = construct_dendrogram(species)
    #print(t.edges)
    #print(t.get_inorder())
    print("Cluster: 1260")
    t.start_cluster_rec(1260)
    print("Cluster: 1350")
    t.start_cluster_rec(1340)
    

if __name__ == "__main__":
    main()
