class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]

    def root(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def find(self, i, j):
        return self.root(i) == self.root(j)

    def union(self, i, j):
        root_i = self.root(i)
        root_j = self.root(j)
        if root_i != root_j:
            self.parent[root_j] = i

    def __str__(self):
        return str(self.parent)

def main():
    x = UnionFind(10)
    string = "Start:\n" + str(x)
    print(string)
    x.union(0,2)
    x.union(1,8)
    x.union(7,8)
    x.union(1,6)
    x.union(0,1)
    string = "End:\n" + str(x)
    print(string)

if __name__ == "__main__":
    main()