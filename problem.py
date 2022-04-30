from node import Node

class Problem:
    def __init__(self, puzzle_cols = 3, init_state = [1, 2, 3, 4, 5, 6, 7, 0, 8], goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]):
        self.init_state = init_state
        self.goal_state = goal_state
        # operators for the blank space (0), if there is a number in that direction
        self.puzzle_cols = puzzle_cols       # num of rows, cols for puzzle

    def get_init_state(self):
        return self.init_state

    def get_goal_state(self):
        return self.goal_state

    def get_puzzle_cols(self):
        return self.puzzle_cols

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
            print("parent = ", node.get_state())
            print("child = ", child.get_state())
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
            node.add_child(child)
        else:
            pass
        
    def expand_node(self, node):
        zero_index = self.get_empty_space_loc(node)

        self.move_left(node, zero_index)
        self.move_right(node, zero_index)
        self.move_up(node, zero_index)
        self.move_down(node, zero_index)

    def print_state(self, node):
        for i in range(len(node.get_state())):
            if i % self.get_puzzle_cols() == 0:
                print()
            else:
                pass
            print(node.get_state()[i], end = " ")
        print()

    def print_node_info(self, node):
        if node.get_direction() != None:
            if node.get_hn() != -1:
                print("The best state to expand with g(n) =", node.get_gn() , " and  h(n) =", node.get_hn())
            else:
                print("The best state to expand with g(n) =", node.get_gn())

            print("Move: " + node.get_direction() + "...")
        else:
            print("Expanding state")
        self.print_state(node)

    def print_solution_path(self, solution):
        for node in solution[::-1]:
            dir = node.get_direction()
            if dir != None:
                print("Move: " + dir + "...")
            else:
                pass
            self.print_state(node)
            print()