from node import Node

class Problem:
    def __init__(self, puzzle_cols = 3, init_state = [1, 2, 3, 4, 5, 6, 7, 0, 8], goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]):
        self.init_state = init_state
        self.goal_state = goal_state
        # operators for the blank space (0), if there is a number in that direction
        self.puzzle_cols = puzzle_cols       # num of rows, cols for puzzle
        self.search_tree = None

    def get_init_state(self):
        return self.init_state

    def get_goal_state(self):
        return self.goal_state

    def get_search_tree(self):
        return self.search_tree

    def set_search_tree(self, st):
        self.search_tree = st

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


    def get_misplaced_tile_gn(self, node, root):
        gn = 0
        gn += node.get_path_cost()

        while (node.get_parent() != None):
            node = node.get_parent()
            gn += node.get_path_cost()
        return gn

    # return the number of misplaced tiles in node 
    def get_misplaced_tile_hn(self, node):
        fn = 0
        node_state = node.get_state()
        for num in self.goal_state:
            if self.goal_state[num] == 0:
                pass
            else:
                if self.goal_state[num] != node_state[num]:
                    fn += 1
                else:
                    pass
        return fn

    def get_misplaced_tile_fn(self, node, root):
        gn = self.get_misplaced_tile_gn(node, root)
        hn = self.get_misplaced_tile_hn(node)
        print(" ******* gn = ", gn, "hn = ", hn)
        return gn + hn 


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
            child.set_depth(node.get_depth() + 1)

            #child.set_cost(child.get_path_cost() + node.get_path_cost())
            print("parent = ", node.get_state())
            print("child = ", child.get_state())

            st_root = self.search_tree.get_root()
            fn = self.get_misplaced_tile_fn(child, st_root)
            child.set_heuristic_cost(fn)
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
            child.set_depth(node.get_depth() + 1)

            st_root = self.search_tree.get_root()
            fn = self.get_misplaced_tile_fn(child, st_root)
            child.set_heuristic_cost(fn)
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
            child.set_depth(node.get_depth() + 1)
            
            st_root = self.search_tree.get_root()
            fn = self.get_misplaced_tile_fn(child, st_root)
            child.set_heuristic_cost(fn)
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
            child.set_depth(node.get_depth() + 1)
        
            st_root = self.search_tree.get_root()
            fn = self.get_misplaced_tile_fn(child, st_root)
            child.set_heuristic_cost(fn)
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
        for node in solution[::-1]:
            dir = node.get_direction()
            if dir != None:
                print("Move: " + dir + "...")
            self.print_state(node)
            print()


    