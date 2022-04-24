import numpy as np

class Node:
    def __init__(self, data = None):
        self.data = data
        self.children = np.array()
        self.parent_data = None

    def getData(self):
        return self.data

    def getParentData(self):
        return self.parent_data

    def getChildrenData(self):
        pass
        # for child in self.children:
        #     print(child.data)

    def is_leaf_node(self):
        return self.children.any()