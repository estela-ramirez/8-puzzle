import re
import numpy as np


"""
Node class has a state (puzzle state), (pointer to) parent, and children attributes
The children attribute is a list that will hold pointers to child nodes
empty space is represented with 9
"""

class Node:
    def __init__(self, state = [1, 2, 3, 4, 5, 6, 7, 8, 9]):
        self.state = state  # state of puzzle 
        self.parent = None
        self.children = []
        self.size = 3       # num of rows, cols for puzzle

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children


    def is_leaf_node(self):
        if len(self.children) == 0:
            return True
        return False

    def print_state(self):
        for i in range(self.state):
            if i % self.size == 0:
                print()
            else:
                pass
            print(self.state[i])

    # return True if Node has goal state, False otherwise
    def is_goal_state(self):
        val = self.state[0]
        for x in range(1, len(self.state)):
            if val > self.state[x]:
                return False
            val = self.state[x]
        return True

    def get_empty_space_loc(self):
        for i in range(len(self.state)):
            if self.state[i] == 9:
                return i 
        return 0

    def move_right(self):
        pass

    def move_left(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass  