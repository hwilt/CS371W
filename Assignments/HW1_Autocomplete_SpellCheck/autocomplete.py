class Autocomplete:
    def __init__(self, filename):
        # Open file, preprocess contents
        # save contents as local variables
        fin = open(filename)
        lines = fin.readlines()
        fin.close()
        self._words = []
        for line in lines:
            _list = line.strip().split("\t")
            _tuple = (str(_list[0]), int(_list[1]))
            self._words.append(_tuple)
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
        '''
        Returns the number of words in the dictionary
        Helper function
        '''
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
        '''
        Returns the index of the last word in the dictionary that starts with prefix
        '''
        # Find the last word in the dictionary that starts with prefix
        # If no such word exists, return -1
        # Otherwise, return index of last word that starts with prefix
        res = -1
        for i in range(firstindex, len(self._words)):
            if self._words[i][0].startswith(prefix):
                #print(self._words[i]) #testing purposes
                res = i
        return res
   
    def all_matches(self, prefix):
        '''
        Returns a list of all words in the dictionary that start with prefix
        '''
        # Find the first word in the dictionary that starts with prefix
        # If no such word exists, return empty list
        # Otherwise, return list of all words that start with prefix
        res = []
        firstindex = self.firstindex(prefix)
        if firstindex == -1:
            res = []
        else:
            lastindex = self.lastindex(prefix, firstindex)
            for i in range(firstindex, lastindex+1):
                res.append(self._words[i])
        return res

def citiesPrefix(prefix):
    a = Autocomplete("cities.txt")
    matches = a.all_matches(prefix)
    matches.sort(key = lambda x: x[1], reverse = True)
    i = 1
    for match in matches:
        print(i, ":", match)
        i += 1

def wordsPrefix(prefix):
    a = Autocomplete("words.txt")
    #print(a.firstindex("urs"), a.lastindex("urs", a.firstindex("urs")))
    matches = a.all_matches(prefix)
    matches.sort(key = lambda x: x[1], reverse = True)
    i = 1
    for match in matches:
        print(i, ":", match)
        i += 1


def main():
    print("Autocomplete Menu:\nEnter 1 for words\nEnter 2 for cities")
    user_input = int(input(""))
    #print(user_input)
    if user_input == 1:
        prefix = input("Enter your prefix: ")
        wordsPrefix(prefix)
    else:
        prefix = input("Enter your prefix: ")
        citiesPrefix(prefix)


if __name__ == "__main__":
    main()

