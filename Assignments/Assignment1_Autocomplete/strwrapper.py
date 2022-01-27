class StrWrapper:
    def __init__(self, s):
        self.s = s
    
    def hash_code(self):
        ## TODO: Fill this in
        return 0 # This is a dummy value

    def __eq__(self, other):
        return self.s == other.s

    def __str__(self):
        return self.s
    
if __name__ == '__main__':
    s1 = StrWrapper("CS 371")
    print(s1 == StrWrapper("CS 37" + "1"))