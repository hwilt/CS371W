class Autocomplete:
    def __init__(self, filename, num_words=-1):
        # Open file, preprocess contents
        # save contents as local variables
        fin = open(filename)
        lines = fin.readlines()
        fin.close()
        self._words = []
        self._numWords = 0
        for line in lines:
            if num_words == -1:
                _list = line.strip().split("\t")
                _tuple = (str(_list[0]), int(_list[1]))
                self._words.append(_tuple)
            else:
                _list = line.strip().split("\t")
                _tuple = (str(_list[0]), int(_list[1]))
                if self._numWords <= num_words:
                    self._words.append(_tuple)
                    self._numWords += 1
        self._words.sort()

    def binarysearch_first(self, arr, target, low=0, high=-1):
        if high == -1:
            high = len(arr)-1
        res = -1
        if low == high:
            string = arr[low][0]
            if string[0:len(target)] == target:
                res = low
        else:
            mid = (low+high)//2
            if arr[mid][0] < target:
                res = self.binarysearch_first(arr, target, mid+1, high)
            else:
                res = self.binarysearch_first(arr, target, low, mid)
        return res
    
    def binarysearch_last(self, arr, target, low=0, high=-1):
        if high == -1:
            high = len(arr)-1
        res = -1
        while low != high:
            mid = (low+high)//2
            string = arr[mid][0]
            if string[0:len(target)] == target:
                res = mid
            elif arr[mid][0] > target:
                res = self.binarysearch_last(arr, target, low, mid-1)
            else:
                res = self.binarysearch_last(arr, target, mid+1, high)
        return res


        """
        if low == high:
            string = arr[low][0]
            if string[0:len(target)] == target:
                res = high
        else:    
            mid = (low+high)//2
            string = arr[mid][0]
            print(string)
            if string[0:len(target)] < target:
                res = self.binarysearch_last(arr, target, mid+1, high)
            else:
                res = self.binarysearch_last(arr, target, low, mid)
        return res
        """

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
        res = self.binarysearch_first(self._words, prefix)
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
            if not self._words[i][0].startswith(prefix):
                #print(self._words[i]) #testing purposes
                res = i - 1
                break
        
        return res
   
    def all_matches(self, prefix):
        '''
        Returns a list of all words in the dictionary that start with prefix
        '''
        # Find the first word in the dictionary that starts with prefix
        # If no such word exists, return empty list
        # Otherwise, return list of all words that start with prefix
        res = []
        firstindex = self.binarysearch_first(self._words,prefix)
        if firstindex == -1:
            res = []
        else:
            lastindex = self.lastindex(prefix, firstindex)
            print(firstindex,lastindex+1)
            res = self._words[firstindex:lastindex+1]
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

