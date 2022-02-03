from strwrapper import *
#from autocomplete import *
from HashTable import *

class SpellChecker():
    def __init__(self, num_words):
        self._numWords = num_words
        #self._autocomplete = Autocomplete("words.txt", num_words)
        self._table = HashTable(num_words//4)
        fin = open("words.txt")
        lines = fin.readlines()
        fin.close()
        i = 0
        for line in lines:
            if i <= num_words:
                word, _wordcount = line.split("\t")
                self._table.add(StrWrapper(word))
                i += 1
            else:
                break

    
    def spellcheck(self, words):
        res = []
        wordlist = words.lower().split(" ")
        for word in wordlist:
            #print(word)
            if self._table.find(StrWrapper(word)):
                    res.append(True)
            else:
                res.append(False)
        return res


def main():
    s = SpellChecker(40000)
    bool_list = s.spellcheck("Hello world tihs is a comptuer science class")
    #bool_list = s.spellcheck("Hello world")
    print(bool_list)

if __name__ == "__main__":
    main()