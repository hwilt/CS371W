class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self._operations = 0
        self._calls = 0

    def root(self, i):
        #self._calls += 1
        while i != self.parent[i]:
            i = self.parent[i]
            self._operations += 1
        return i

    def find(self, i, j):
        self._calls += 1
        return self.root(i) == self.root(j)

    def union(self, i, j):
        self._calls += 1
        root_i = self.root(i)
        root_j = self.root(j)
        if root_i != root_j:
            self._operations += 1
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

    print(x._calls)
    print(x._operations)

if __name__ == "__main__":
    main()