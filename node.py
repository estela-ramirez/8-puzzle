"""
Node class has a state (puzzle state), (pointer to) parent, and children attributes
The children attribute is a list that will hold pointers to child nodes
empty space is represented with 0
"""

class Node:
    def __init__(self, state = [1, 2, 3, 4, 5, 6, 7, 0, 8]):
        self.state = state  # state of puzzle 
        self.parent = None
        self.children = []
        self.cost = 1
        self.direction = None 

    # make node a comparable object 
    def __gt__(self, node2):
        return self.cost > node2.cost

    def __eq__(self, node2):
        if node2 != None:
            return self.state == node2.state

    def __str__(self):
        return ','.join(str(e) for e in self.state)

    def __repr__(self):
        return repr(self.state)


#### for testing   
    def get_direction(self):
        return self.direction

    def set_direction(self, dir):
        self.direction = dir
#### for testing  

    def get_state(self):
        return self.state.copy()

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children.copy()

    def set_parent(self, parent):
        self.parent = parent

    def get_cost(self):
        return self.cost

    def add_child(self, child):
        # add pointer to parent
        self.children.append(child)
        # update child's cost

    def set_cost(self, cost):
        self.cost = cost