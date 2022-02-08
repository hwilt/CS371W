class MyDisjointSet:
    def __init__(self, N):
        self.N = N
        #self.parent = [{i} for i in range(N)]
        self.parent = [{0,1},{2,3},{4,5},{6,7},{8,9}]
        print(self.parent)
    
    def find(self, i, j):
        """
        Return true if i and j are in the same component, or
        false otherwise
        
        Parameters
        ----------
        i: int
            Index of first element
        j: int
            Index of second element
        """
        res = False
        for x in self.parent:
            if len(x) > 1:
                if i in x and j in x:
                    res = True
                    break
        return res
    
    def union(self, i, j):
        """
        Merge the two sets containing i and j, or do nothing if they're
        in the same set
        Parameters
        ----------
        i: int
            Index of first element
        j: int
            Index of second element
        """
        if self.find(i,j):
            pass
        else:
            pass





s = MyDisjointSet(10)
print(s.find(0,1))