class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

def traverse(N):
    if N.left:
        traverse(N.left)
    print(N.value, end='.')
    if N.right:
        traverse(N.right)

def make_tree():
    T = BinaryTree()
    T.root = TreeNode(9)
    T.root.left = TreeNode(4)
    ## TODO: Finish this
    T.root.right = TreeNode(20)
    T.root.left.left = TreeNode(1)
    T.root.left.right = TreeNode(8)
    T.root.right.left = TreeNode(15)
    T.root.right.right = TreeNode(25)
    return T

T = make_tree()
traverse(T.root)