from strwrapper import *
from autocomplete import *
from HashTable import *

class SpellChecker():
    def __init__(self, num_words):
        self._numWords = num_words
        self._autocomplete = Autocomplete("words.txt", num_words)
        #TODO: HASHTABLE???

    
    def spellcheck(self, words):
        res = []
        wordlist = words.lower().split(" ")
        for word in wordlist:
            matches = self._autocomplete.all_matches(word)
            found = False
            for match in matches:
                if match[0] == word and match[1] >= self._numWords:
                    found = True
                    break
            if found:
                res.append(True)
            else:
                res.append(False)
        return res


s = SpellChecker(40000)
bool_list = s.spellcheck("Hello world tihs is a comptuer science class")
#bool_list = s.spellcheck("Hello world")
print(bool_list)