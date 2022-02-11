import numpy as np

class ArrayList:
    def __init__(self, initial=10, fac=0.3):
        """
        Parameters
        -----------
        initial: int
            Size of initial array
        fac: float
            Factor at which to halve the array
        """
        self.arr = np.zeros(initial)
        self.N = 0
        self.fac = fac
    
    def add(self, x):
        ## TODO: This will eventually go out of bounds!
        # if the new element will be at the limit or beyond,
        # then double the size of the array
        if self.N == len(self.arr):
            # make new arr with the length * 2
            newarr = np.zeros(int(len(self.arr)*2))
            newarr[0:self.N] = self.arr
            self.arr = newarr
        self.arr[self.N] = x
        self.N += 1
        ## TODO: Need to resize array and copy things
        ## If array runs out of space, create a new array
        ## with double the size using np.zeros, and copy
        ## everything over
    
    def remove(self, idx):
        """
        Remove the element at index idx and shift everything
        over to the left
        
        If you are using fewer than int(self.N*fac) elements, 
        then halve the array length 
        """
        ## TODO: Fill this in
        #np.delete(self.arr, idx) 
        # if the array is less than the factor, halve the array
        minlen = int(self.N*self.fac)
        if self.N == minlen:
            newarr = np.zeros(int(len(self.arr)/2))
        for i in range(idx+1, self.N):
            self.arr[i-1] = self.arr[i]
        self.N -= 1
        

    def __str__(self):
        s = "["
        for i in range(self.N):
            s += "{}".format(self.arr[i])
            if i < self.N-1:
                s += ", "
        s += "]"
        return s
    
mylist = ArrayList()
np.random.seed(0)
# Add 5 random numbers
for idx in np.random.randint(0, 100, 11):
    mylist.add(idx)
print(mylist)

## TODO: Test removing some indices

mylist.remove(4)
mylist.remove(7)
print(mylist)