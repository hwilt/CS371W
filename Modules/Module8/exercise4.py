class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def contains(self, value):
        res = False
        if self.value == value:
            res = True
        else:
            if self.left:
                res = self.left.contains(value)
            ## TODO: Recurse on the right child
            if self.right and not res:
                res = self.right.contains(value)
        return res
        

class BinaryTree(object):
    def __init__(self):
        self.root = None
    
    def contains(self, value):
        res = False
        if self.root:
            res = self.root.contains(value)
        return res


def make_left_subtree():
    node = TreeNode(7)
    node.left = TreeNode(3)
    node.right = TreeNode(9)
    node.right.left = TreeNode(8)
    return node

def make_right_subtree():
    node = TreeNode(16)
    node.left = TreeNode(11)
    node.right = TreeNode(20)
    node.left.right = TreeNode(14)
    node.left.right.right = TreeNode(15)
    node.left.right.left = TreeNode(13)
    node.left.right.left.left = TreeNode(12)
    return node

def make_tree():
    T = BinaryTree()
    T.root = TreeNode(10)
    T.root.left = make_left_subtree()
    T.root.right = make_right_subtree()
    return T

T = make_tree()
print(T.contains(11), end='.')
print(T.contains(12), end='.')
print(T.contains(2), end='.')
print(T.contains(0), end='.')
print(T.contains(19.5), end='.')
print(T.contains(20), end='.')
print(T.contains(17), end='.')