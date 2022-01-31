from harrypotter import *

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
        pass
    
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


llist = LinkedList()
wizards = get_all_wizards()
for w in wizards:
    llist.add(w)
hermione = Wizard("Hermione Granger", 4, 15, 1990)
barack = Wizard("Barack Obama", 8, 4, 1961)
print(hermione, "in list: ", llist.find(hermione))
print(barack, "in list: ", llist.find(barack))

print(llist)
