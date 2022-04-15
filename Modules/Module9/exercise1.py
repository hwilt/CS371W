from collections import deque

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
        nodes = deque()
        # First, add all of the leaf nodes with the requested characters
        for c in chars:
            nodes.append(TreeNode(c))
        while len(nodes) > 1:
            # Take first two out of line
            n1 = nodes.popleft()
            n2 = nodes.popleft()
            # Merge the two by making a new node
            
            ## TODO: Fill this in
            new_node = TreeNode()
            new_node.left = n1
            new_node.right = n2
            nodes.append(new_node)
            # this is correct, just need to submit it on campus
            # Add new node to the back of the line
            
            ## TODO: Fill this in
            
        # Last node left is root
        self.root = nodes.pop()

    def get_codebook(self):
        codebook = {}
        if self.root:
            self.root.build_codebook(codebook, [])
        return codebook

chars = ['y', 'r', 't', 'u', 'o', 'd', 'w', 'k', 'v', 'e', 'c', 'x', 'g', 's', 'n', 'h', 'z', 'b', 'q', 'a', 'p', '.', ' ', 'j', 'i', 'm', 'l', 'f']
T = BCBTree(chars)
print(T.get_codebook())
