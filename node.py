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
        self.path_cost = 1
        # heuristic_cost is == g(n) with UCS, cost
        # heuristic_cost is f(n) = g(n) + h(n) for A star
        self.heuristic_cost = 0  
        self.gn = 0
        self.hn = -1 
        self.depth = 0
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

    # getter methods
    def get_direction(self):
        return self.direction

    def get_state(self):
        return self.state.copy()

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children.copy()

    def get_path_cost(self):
        return self.path_cost

    def get_gn(self):
        return self.gn
    
    def get_hn(self):
        return self.hn

    def get_heuristic_cost(self):
        return self.heuristic_cost
        
    def get_depth(self):
        return self.depth

    # setter methods 
    def set_direction(self, dir):
        self.direction = dir 

    def set_parent(self, parent):
        self.parent = parent

    def set_path_cost(self, pc):
        self.path_cost = pc

    def set_gn(self, gn):
        self.gn = gn 

    def set_hn(self, hn):
        self.hn = hn

    def set_heuristic_cost(self, hc):
        self.heuristic_cost = hc

    def set_depth(self, depth):
        self.depth = depth

    # helper methods
    def is_leaf_node(self):
        if len(self.get_children()) == 0:
            return True
        return False
        
    # if Node's state matches Problem's goal state, returns True, False otherwise
    def is_goal_state(self, goal_state):
        if goal_state == self.get_state():
            return True
        return False
    
    # set pointer to parent, add child in parent's list of children
    # set child depth's to +1 that of the parent's
    def add_child(self, child):
        child.set_parent(self)
        self.children.append(child)
        child.set_depth(self.get_depth() + 1)

    
            