# Single list, each element is the ID of the correspanding object
class MyDisjointSet:
    def __init__(self, N):
        self.N = N
        self._ids = list(range(N))
    
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
        return False #TODO: This is a dummy value
    
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
        #if i and j have different IDs, merge them
        idx_i = self._ids[i]
        idx_j = self._ids[j]
        if idx_i != idx_j:
            #merge the two sets
            for k, id_k in enumerate(self._ids):
                if id_k == idx_j:
                    self._ids[k] = idx_i