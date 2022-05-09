class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


    
    def add(self, key):
        ret = self
        if key < self.key:
            if self.left:
                self.left = self.left.add(key)
            else:
                self.left = TreeNode(key)
        elif key > self.key:
            if self.right:
                self.right = self.right.add(key)
            else:
                self.right = TreeNode(key)
        return ret

    def inorder(self, key_list):
        if self.left:
            self.left.inorder(key_list)

        key_list.append(self.key)

        if self.right:
            self.right.inorder(key_list)

    def preorder(self, key_list):

        key_list.append(self.key)
        #print(self.key)

        if self.left:
            self.left.preorder(key_list)
        if self.right:
            self.right.preorder(key_list)


    def postorder(self, key_list):
        if self.left:
            self.left.postorder(key_list)
        if self.right:
            self.right.postorder(key_list)

        key_list.append(self.key)
        
            


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root:
            self.root = self.root.add(key)
        else:
            self.root = TreeNode(key)

    def inorder(self):
        key_list = []
        if self.root:
            self.root.inorder(key_list)
        return key_list

    def preorder(self):
        key_list = []
        if self.root:
            self.root.preorder(key_list)
        return key_list

    def postorder(self):
        key_list = []
        if self.root:
            self.root.postorder(key_list)
        return key_list



def topToBottom(root):
    nodes = dict()

    def recurse(node, level, depth, minlevel = 0, maxlevel = 0):
        minlevel = min(minlevel, level)
        minlevel = max(minlevel, level)
        
        if level not in nodes:
            nodes[level] = []
        nodes[level].append((depth, node.key))
        
        recurse(node.left, level-1, depth+1)
        recurse(node.right, level+1, depth+1)

    recurse(root, 0, 0)

    ret = []

    for i in range(minlevel, maxlevel-1):
        col = sorted(nodes[i])
        col = [v for _, v in col]
        ret.append(col)


    return ret




def main():
    T = BinaryTree()
    for i in [10, 7, 16, 3, 9, 11, 20]:
        T.add(i)
    print("inorder: " + str(T.inorder()))
    print("preorder: " + str(T.preorder()))
    print("postorder: " + str(T.postorder()))
    print("top to bottom: " + str(topToBottom(T.root)))

main()