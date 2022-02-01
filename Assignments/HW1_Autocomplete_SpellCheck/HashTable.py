class Node:
    def __init__(self, obj):
        self.obj = obj
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, obj):
        # Make a new container for this object
        new_node = Node(obj)
        # This new node points to what is currently the head
        new_node.next = self.head
        # The head now points to the new node
        self.head = new_node
    
    def remove(self, obj):
        ###TODO: REMOVE AN OBJECT FROM THE LIST
        node = self.head
        prev = None
        found = False
        while node and not found:
            if node.obj == obj:
                found = True
            else:
                prev = node
                node = node.next
        if found:
            if prev:
                prev.next = node.next
            else:
                self.head = node.next
    
    def find(self, obj):
        """
        Return True if obj is there, False otherwise
        """
        node = self.head
        found = False
        # Note that "while node" is True as long as 
        # node is not None
        while node and not found:
            # Note that we had to implement __eq__ for wizards
            # in order for this to make sense
            if node.obj == obj: 
                found = True
            else:
                # Keep chasing arrows until we get to the end and
                # there's nothing left
                node = node.next
        return found
    
    def __len__(self):
        """
        Like java's size()
        """
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def __str__(self):
        """
        Like java's toString()
        """
        node = self.head
        s = ""
        while node:
            s += str(node.obj) + " -> "
            node = node.next
        return s

class HashTable:
    def __init__(self, n_bins):
        self._n_bins = n_bins
        self._bins = []
        for i in range(n_bins):
            self._bins.append(LinkedList())

    def __len__(self):
        return self._n_bins

    def add(self, obj):
        """
        Add obj to the hash table
        """
        hashcode = obj.hash_code()
        self._bins[hashcode%self._n_bins].add(obj)

    def remove(self, obj):
        """
        Remove obj from the hash table
        """
        hashcode = obj.hash_code()
        self._bins[hashcode%self._n_bins].remove(obj)
        
    def find(self, obj):
        """
        Return True if obj is in the hash table, False otherwise
        """
        hashcode = obj.hash_code()
        return self._bins[hashcode%self._n_bins].find(obj)
    
