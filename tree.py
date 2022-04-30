from node import Node

class Tree:
    def __init__(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def get_solution_path(self, leaf_node):
        path = []
        path.append(leaf_node)
        curr_node = leaf_node

        while (curr_node.get_parent() != None):
            curr_node = curr_node.get_parent()
            path.append(curr_node)
        
        return path
