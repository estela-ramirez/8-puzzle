from node import Node

class Problem:
    def __init__(self, init_state = [1, 2, 3, 4, 8, 0, 7, 6, 5], goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]):
        self.init_state = init_state
        self.goal_state = goal_state
        # operators for the blank space (0), if there is a number in that direction
        self.puzzle_cols = 3       # num of rows, cols for puzzle

    def get_init_state(self):
        return self.init_state

    def get_goal_state(self):
        return self.goal_state

    def get_operators(self):
        return self.operators


    # if Node's state matches Problem's goal state, returns True, False otherwise
    def is_goal_state(self, node):
        if self.goal_state == node.get_state():
            return True
        return False


    def is_leaf_node(self, node):
        if len(node.get_children()) == 0:
            return True
        return False

    def print_state(self, node):
        for i in range(len(node.get_state())):
            if i % self.puzzle_cols == 0:
                print()
            else:
                pass
            print(node.get_state()[i], end = " ")
        print()

    # returns the index of the empty space (0) in the node's state/ puzzle
    def get_empty_space_loc(self, node):
        for i in range(len(node.get_state())):
            if node.get_state()[i] == 0:
                return i
            else:
                pass 
        return 0


    def move_left(self, node, zero_index):
        if zero_index % self.puzzle_cols  > 0:

            new_state = node.get_state()

            # swap 0 and the number to it's left 
            temp = new_state[zero_index] 
            new_state[zero_index] = new_state[zero_index - 1]  
            new_state[zero_index - 1] = temp 

            child = Node(new_state)
            child.set_direction("left")
            child.set_parent(node)
            # child.set_cost(node.get_cost() + child.get_cost())
            node.add_child(child)
        else:
            pass

    def move_right(self, node, zero_index):
        if zero_index % self.puzzle_cols  < self.puzzle_cols - 1:
            
            new_state = node.get_state()

            # swap 0 and the number to it's right
            temp = new_state[zero_index] 
            new_state[zero_index] = new_state[zero_index + 1]  
            new_state[zero_index + 1] = temp 

            child = Node(new_state)
            child.set_direction("right")
            child.set_parent(node)
            node.add_child(child)
        else:
            pass

    def move_up(self, node, zero_index):
        if zero_index - self.puzzle_cols  >= 0:

            new_state = node.get_state()

            # swap 0 and the number to above it
            temp = new_state[zero_index] 
            new_state[zero_index] = new_state[zero_index - self.puzzle_cols]  
            new_state[zero_index - self.puzzle_cols] = temp 

            child = Node(new_state)
            child.set_direction("up")
            child.set_parent(node)
            node.add_child(child)
        else:
            pass

    def move_down(self, node, zero_index):

        puzzle_len = self.puzzle_cols * self.puzzle_cols

        if zero_index + self.puzzle_cols  < puzzle_len:

            new_state = node.get_state()

            # swap 0 and the number below it
            temp = new_state[zero_index] 
            new_state[zero_index] = new_state[zero_index + self.puzzle_cols]  
            new_state[zero_index + self.puzzle_cols] = temp 

            child = Node(new_state)
            child.set_direction("down")
            child.set_parent(node)
            node.add_child(child)
        else:
            pass
        
    def expand_node(self, node):
        zero_index = self.get_empty_space_loc(node)

        self.move_left(node, zero_index)
        self.move_right(node, zero_index)
        self.move_up(node, zero_index)
        self.move_down(node, zero_index)
        
        
    
    def get_solution_path(self, leaf_node):
        path = []
        path.append(leaf_node)
        curr_node = leaf_node

        while (curr_node.get_parent() != None):
            curr_node = curr_node.get_parent()
            path.append(curr_node)
        
        return path

    def print_solution_path(self, solution):
        for node in solution:
            self.print_state(node)
            print()