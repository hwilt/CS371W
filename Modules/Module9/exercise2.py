from collections import deque

class TreeNode(object):
    def __init__(self, key = None):
        self.key = key
        self.left = None
        self.right = None

class BCBTree(object):
    def __init__(self, chars):
        nodes = deque()
        for c in chars:
            nodes.append(TreeNode(c))
        while len(nodes) > 1:
            # Take first two out of line
            n1 = nodes.popleft()
            n2 = nodes.popleft()
            # Merge the two by making a new node
            n12 = TreeNode()
            n12.left = n1
            n12.right = n2
            # Add new node to the back of the line
            nodes.append(n12)
        # Last node left is root
        self.root = nodes.pop()

    def decode(self, s):
        ret = ""
        if self.root:
            # A node that stores where we are as we're walking the tree
            node = self.root
            for b in s: # Loop through every 1/0 in the encoded string
                if node.key:
                    ## TODO: Fill this in
                    ## Add on this node's character to ret
                    ## then go back to the root
                    ret += node.key
                    node = self.root
                ## TODO: Fill this in
                ## Move node to the left or right depending on b
                if b == "0":
                    node = node.left
                else:
                    node = node.right
            if node.key:
                ret += node.key
        return ret

chars = ['y', 'r', 't', 'u', 'o', 'd', 'w', 'k', 'v', 'e', 'c', 'x', 'g', 's', 'n', 'h', 'z', 'b', 'q', 'a', 'p', '.', ' ', 'j', 'i', 'm', 'l', 'f']
T = BCBTree(chars)
s1 = "1011110001001000100110011110011100110001001001001101"
s2 = "0000111100010011001000010001111101001010101"
print(T.decode(s1)+"."+T.decode(s2))