class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

def make_left_subtree():
    node = TreeNode(7)
    node.left = TreeNode(3)
    node.right = TreeNode(9)
    node.right.left = TreeNode(8)
    return node

def make_right_subtree():
    node = TreeNode(15)
    node.left = TreeNode(12)
    node.right = TreeNode(20)
    node.left.right = TreeNode(14)
    node.left.right.left = TreeNode(13)
    return node;

def make_tree():
    T = BinaryTree()
    T.root = TreeNode(10)
    T.root.left = make_left_subtree()
    T.root.right = make_right_subtree()
    return T

def preorder(node):
    ## TODO: Finish this.  As a stopping
    ## condition, be sure to only visit a child
    ## node if it is not None.
    print(node.value, end='.')
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

T = make_tree()
preorder(T.root)