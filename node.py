"""
Node class has a state (puzzle state), (pointer to) parent, and children attributes
The children attribute is a list that will hold pointers to child nodes
empty space is represented with 0
"""

class Node:
    def __init__(self, state = [1, 2, 3, 4, 5, 6, 7, 8, 0]):
        self.state = state  # state of puzzle 
        self.parent = None
        self.children = []
        self.cost = 1
        
    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def set_parent(self, parent):
        self.parent = parent

    def get_cost(self):
        return self.cost

    def add_child(self, child):
        self.children.append(child)

    def set_cost(self, cost):
        self.cost = cost