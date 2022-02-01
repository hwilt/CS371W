class Autocomplete:
    def __init__(self, filename):
        # Open file, preprocess contents
        # save contents as local variables
        fin = open(filename)
        lines = fin.readlines()
        fin.close()
        self._words = []
        for line in lines:
            self._words.append(line.strip().split("\t"))
        self._words.sort()
    
    def binarysearch(self, arr, target, low=0, high=-1):
        if high == -1:
            high = len(arr)-1
        res = -1
        if low == high:
            if arr[low][0].startswith(target):
                res = low
        else:
            mid = (low+high)//2
            #print(arr[mid])
            if arr[mid][0] < target:
                res = self.binarysearch(arr, target, mid+1, high)
            else:
                res = self.binarysearch(arr, target, low, mid)
        return res
    
    def __len__(self):
        return len(self._words)

    def returnlist(self):
        '''
        Returns a list of all words in the dictionary
        Helper function for testing
        '''
        return self._words

    def firstindex(self, prefix):
        '''
        Returns the index of the first word in the dictionary that starts with prefix
        '''
        # Find the first word in the dictionary that starts with prefix
        # If no such word exists, return -1
        # Otherwise, return index of first word that starts with prefix
        res = -1
        res = self.binarysearch(self._words,prefix)
        return res
    
    def lastindex(self, prefix, firstindex):
        res = -1
        for i in range(firstindex, len(self._words)):
            if self._words[i][0].startswith(prefix):
                print(self._words[i])
                res = i - 1
        return res

    def other_method(self):
        #... Binary search queries should happen in different internal methods
        pass
   
    def all_matches(self, prefix):
        '''
        Returns a list of all words in the dictionary that start with prefix
        '''
        # Find the first word in the dictionary that starts with prefix
        # If no such word exists, return empty list
        # Otherwise, return list of all words that start with prefix
        res = []
        return res
        

        
        

a = Autocomplete("words.txt")
print(a.firstindex("urs"), a.lastindex("urs", a.firstindex("urs")))
#matches = a.all_matches("urs")