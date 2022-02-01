from strwrapper import *
from autocomplete import *
from HashTable import *

class SpellCheck():
    def __init__(self, num_words):
        self._num_words = num_words
    
    def check(self, word):
        return False


s = SpellCheck(40000)
bool_list = s.spellcheck("Hello world tihs is a comptuer science class")
print(bool_list)