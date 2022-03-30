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

def inorder(node):
    ## TODO: Finish this.  As a stopping
    ## condition, be sure to only visit a child
    ## node if it is not None.  The way to see if
    ## an object "obj" in python is not none is 
    ## to simply say
    ## if obj:
    ##    do something
    ##
    ## If you have a list, you can use the "in"
    ## operator to check if an item is in the list.
    ##
    ## If you have a dictionary, you can use the
    ## "in" operator to check if a key is in the
    ## dictionary.
    if node.left:
        inorder(node.left)
    print(node.value, end='.')
    if node.right:
        inorder(node.right)

T = make_tree()
inorder(T.root)