# Coding Basics
# LinkedLists

from abc import ABC, abstractmethod
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LinkedList(ABC): # Doubly linked lists inherit LinkedLists
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # The NODE is the primary storage of data in a linked list
    class Node:
        # Constructor
        def __init__(self, value, nextNode=None):
            self.value = value
            self.next = nextNode
        # In-code and in-shell representation
        def __repr__(self):
            return f"Node ({self.value})"
        # Comparison methods (compare values only, not pointers)
        def __lt__(self, other):
            return self.value < other.value
        def __gt__(self, other):
            return self.value > other.value
        def __le__(self, other):
            return self.value <= other.value
        def __ge__(self, other):
            return self.value >= other.value
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # These are BASIC class methods that dont necessarily modify the lists
    # Constructor
    def __init__(self):
        self.head = None
    # In-code and in-shell representation
    def __repr__(self):
        # Basic method of traversing through the list
        string = ""
        for node in self:
            string += node.value + " -> "
        string += "None"
        return string
    # Status methods
    @property
    def tail(self): # Tail of the list is a property method that has to be re-calculated
        return list(self)[-1]
    @property
    def isEmpty(self):
        return self.head == None
    def __len__(self):
        return len(list(self))
    def __copy__(self): # Creates a deep copy of the entire list
        pass
    def __reverse__(self): # Creates a deep copy of the entire list, reversed
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # These are value INSERTION methods
    # Inserting values to the head, with the option to insert before a specific value
    def insert(self, value, beforeVal=self.head.value):
        if self.isEmpty and beforeVal == None: # Short-circuit for an empty list
            self.head = Node(value)
            return
        if beforeVal == None: # Short-circuit for "inserting" to the end (appending)
            self.append(value)
            return
        if beforeVal == self.head.value: # Short circuit for actually performing the operation
            self.head = Node(value, self.head)
            return

        for node in self: # Looping through the linked list
            if node.next.value == beforeVal:
                node.next = Node(value, node.next)
                return
        # A beforeVal has not been found in the list
        return "Chosen insertion value does not exist in this list."
    # Append values to the end, with the option to append after a specific value
    def append(self, value, afterVal=self.tail.value):
        if self.isEmpty and afterVal == None: # Short-circuit for an empty list
            self.head = Node(value)
            return
        if afterVal == None: # Short-circuit for "appending" to the beginnning (inserting)
            self.insert(value)
            return

        for node in self: # Looping through the linked list
            if node.value == afterVal:
                node.next = Node(value, node.next)
        # An afterVal has not been found in the list
        return "Chosen append value does not exist in this list."
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # These are value DELETION methods
    # Pop and remove values
        # tail = self.getTail()
        # if self.next == tail:
            # self.next = None
            # return tail.value
        # else:
            # return self.next.trimTail()
    # Remove a specific value
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # These are ITERATION methods to step through the lists
    # Creates the first position of the iterable object of the list
    def __iter__(self):
        self.current = self.head # Stores the starting point value
        return self
    # Steps through the list
    def __next__(self):
        current = self.current
        if not current.next: # Short-circuit the end of the list/empty list
            raise StopIteration
        self.current = current.next
        return current
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class DoublyLinkedList(LinkedList):
    pass
