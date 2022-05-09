class trieNode:
    def __init__(self):
        #self.key = None
        self.children = dict() # {'t': triNode('t')}
        self.fullword = False



class Trie:
    def __init__(self):
        self.root = trieNode()
        

    def add_word(self, word):
        # example: bids
        node = self.root
        for letter in word:
            #print(letter)
            if letter in node.children:
                node = node.children[letter]
            else:
                node.children[letter] = trieNode()
                node = node.children[letter]

        node.fullword = True

    def contains_word(self, word):
        # returns true if it is in the structure
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            else:
                node = node.children[letter]
        
        return node.fullword
            
    
    def recursive(self, node, expression, word, words):
        if len(expression) == len(word):
            if node.fullword:
                words.append(word)
        else:
            letter = expression[len(word)]
            if letter != '.' and letter in node.children:
                self.recursive(node.children[letter], expression, word+letter, words)
            elif letter == '.':
                for child in node.children:
                    self.recursive(node.children[child], expression, word+child, words)

    #recursive
    #Create a method get_words that looks up a string with a special format, where "." is the "wildcard"
    #Ex) T.get_words("b...y"), it should return ["buddy", "belly"]
    #Ex) T.get_word(".e.") returns ["see"]
    def get_words(self, expression):
        # have a list to hold all words
        node = self.root
        words = []
        self.recursive(node, expression, "", words)
        return words

            
                


import numpy as np
T = Trie()
np.random.seed(0)
words = ["be", "bear", "bell", "belly", "belt", "belted", "bid", "big", "bigger", "bus", "bull", "buy", "bud", "buddy", "see", "sell", "stop", "stock"]
words = [words[i] for i in np.random.permutation(len(words))]
for w in words:
    T.add_word(w)
"""
for w in words + ["bi", "sto", "bel", "henry"]:
    print(w, T.contains_word(w))"""

print(T.get_words("b...y"))
print(T.get_words(".e."))
print(T.get_words("henry"))