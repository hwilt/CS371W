from heapq import heappush, heappop

class TreeNode(object):
    def __init__(self, key = None):
        self.key = key
        self.left = None
        self.right = None

    def build_codebook(self, codebook, bstr):
        if self.key:
            codebook[self.key] = "".join(bstr)
        else:
            bstr.append("0")
            self.left.build_codebook(codebook, bstr)
            bstr.pop()
            bstr.append("1")
            self.right.build_codebook(codebook, bstr)
            bstr.pop()

class BCBTree(object):
    def __init__(self, chars):
        pass # We're skipping this here since we're focused on the Huffman tree

    def get_codebook(self):
        codebook = {}
        if self.root:
            self.root.build_codebook(codebook, [])
        return codebook

# Inherit from the BCBTree class.  The only thing that
# changes is the constructor
class HuffmanTree(BCBTree): 
    def __init__(self, counts):
        nodes = []
        for key, count in counts.items():
            heappush(nodes, (count, TreeNode(key)))
        while len(nodes) > 1:
            (count1, n1) = heappop(nodes)
            (count2, n2) = heappop(nodes)
            ## TODO: Create a new node with n1 on the left and n2
            ## on the right.  Then, add this node to the heap with
            ## a count equal to the sum of the counts of the two nodes
            ## that were just popped.
            new_node = TreeNode()
            new_node.left = n1
            new_node.right = n2
            heappush(nodes, (count1 + count2, new_node))
        self.root = nodes[0][1]

counts = {'t': 247577342738, 'h': 106367962556, 'e': 349588141984, 'o': 228025627088, 'f': 61328927423, 'a': 243662684512, 'n': 207910712159, 'd': 107605388542, 'i': 223353030415, 'r': 201896673641, 's': 207080253606, 'b': 49798922187, 'y': 52941043438, 'w': 44294405401, 'u': 86950627146, 'm': 84155576549, 'l': 130649920346, 'v': 34402346309, 'c': 113913698859, 'p': 77553040250, 'g': 63045208347, 'k': 24380950863, 'x': 9151143994, 'j': 7637833834, 'z': 4192477980, 'q': 4218467887, ' ': 349588141985, '.': 69917628396}
T = HuffmanTree(counts)
print(T.get_codebook())