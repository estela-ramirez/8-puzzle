from problem import Problem
from tree import Tree
from node import Node
import math

class A_star:
    def __init__(self, problem, hc):
        self.problem = problem
        # 2 will be misplaced tile, # 3 will be euclidian dist
        self.heuristic_choice = hc  
        self._search_tree = None
        self._frontier = []
        self._explored = []

        self.max_nodes_in_frontier = 1
        self.sol_depth = 0


    def get_heuristic_choice(self):
        return self.heuristic_choice

    def get_num_exanded_nodes(self):
        return len(self._explored)

    def get_max_nodes_in_frontier(self):
        return self.max_nodes_in_frontier
    
    def get_sol_depth(self):
        return self.sol_depth

    def _init_frontier(self):
        init_state = self.problem.get_init_state()
        root = Node(init_state)
        root.set_path_cost(0)
        self._search_tree = Tree(root)
    
        self._frontier.append(root)

    def _contains(self, iterable, child):
        for node in iterable:
            if node.get_state() == child.get_state():
                return True
            else:
                pass
        return False

    def _update_max_nodes_in_frontier(self):
        nodes_in_frontier = len(self._frontier)
        if nodes_in_frontier > self.max_nodes_in_frontier:
            self.max_nodes_in_frontier = nodes_in_frontier
        else:
            pass

    # g(n) for this is really just the depth of the node
    # but it's the cost of each node going up until you reach the root
    # starting from the passed in node
    def calculate_gn(self, node, root):
        gn = 0
        gn += node.get_path_cost()

        while (node.get_parent() != None):
            node = node.get_parent()
            gn += node.get_path_cost()
        return gn

    # return the number of misplaced tiles in node 
    def calculate_misplaced_tile_hn(self, node):
        hn = 0
        node_state = node.get_state()
        prob_goal_state = self.problem.get_goal_state()
        for num in prob_goal_state:
            if prob_goal_state[num] == 0:
                pass
            else:
                if prob_goal_state[num] != node_state[num]:
                    hn += 1
                else:
                    pass
        return hn

    # return the column in which the value at state[index] is at
    # return -1 if this index is not within range of the state
    def _get_column(self, state, index):
        num_cols = int(math.sqrt(len(state)))

        for col in range(num_cols):
            for k in range(num_cols):
                test_col = col
                test_col = test_col + k * num_cols

                if test_col == index:
                    # find the col where the num is at
                    return col
                else:
                    pass
        return -1 

    # return the row in which the value at state[index] is at
    # return -1 if this index is not within range of the state
    def _get_row(self, state, index):
        num_rows = int(math.sqrt(len(state)))

        for row in range(num_rows):
            if index < num_rows * (row + 1):
                return row
            else:
                pass

        return -1

    # make a copy of the state, so it doesn't get modified
    # if the number at state[index] is able to be moved to the left
    # swap it with the number in the row to the left
    # return the copied modified state
    def _move_left(self, state, index):
        num_cols = int(math.sqrt(len(state)))
        state_copy = state.copy()
        if index % num_cols  > 0:
            temp = state_copy[index]
            state_copy[index] = state_copy[index - 1]
            state_copy[index - 1] = temp
        else:
            print("can't move left")
        return state_copy

    # make a copy of the state, so it doesn't get modified
    # if the number at state[index] is able to be moved to the right
    # swap it with the number in the row to the right
    # return the copied modified state
    def _move_right(self, state, index):
        num_cols = int(math.sqrt(len(state)))
        state_copy = state.copy()
        if index % num_cols  < num_cols - 1:
            temp = state_copy[index]
            state_copy[index] = state_copy[index + 1]
            state_copy[index + 1] = temp
        else:
            print("can't move right")
        return state_copy

    # make a copy of the state, so it doesn't get modified
    # if the number at state[index] is able to be moved up
    # swap it with the number in the row above
    # return the copied modified state
    def _move_up(self, state, index):
        
        num_rows = int(math.sqrt(len(state)))
        state_copy = state.copy()
        # if index > num_rows:
        if index - num_rows  >= 0:
            temp = state_copy[index]
            state_copy[index] = state_copy[index - num_rows]
            state_copy[index - num_rows] = temp
        else:
            print("can't move up")
        return state_copy

    # make a copy of the state, so it doesn't get modified
    # if the number at state[index] is able to be moved down
    # swap it with the number in the row below 
    # return the copied modified state
    def _move_down(self, state, index):
        num_rows = int(math.sqrt(len(state)))
        state_copy = state.copy()
        # if index < len(state) - num_rows:
        if index + num_rows  < len(state):
            temp = state_copy[index]
            state_copy[index] = state_copy[index + num_rows]
            state_copy[index + num_rows] = temp
        else:
            print("can't move down")
        return state_copy

    # return the number of moves in the y direction needed to get the num 
    # at state[index] on the same column as goal[goal_index]

    def _get_x_moves(self, state, goal, state_index, goal_index):
        num_cols = int(math.sqrt(len(state)))
        curr_col = self._get_column(state, state_index)
        goal_col = self._get_column(goal, goal_index)
        x_moves = 0
        state_copy = state.copy()
        for col in range(num_cols):
            if curr_col < goal_col:
                # print("right")
                state_copy = self._move_right(state_copy, state_index)
                curr_col = self._get_column(state_copy, state_index + 1)
            elif curr_col > goal_col:
                # print("left")
                state_copy = self._move_left(state_copy, state_index)
                curr_col = self._get_column(state_copy, state_index - 1)
            else:
                break
            x_moves += 1
        return x_moves

    # return the number of moves in the y direction needed to get the num 
    # at state[index] on the same row as goal[goal_index]
    def _get_y_moves(self, state, goal, state_index, goal_index):
        num_rows = int(math.sqrt(len(state)))
        curr_row = self._get_row(state, state_index)
        goal_row = self._get_row(goal, goal_index)
        y_moves = 0
        state_copy = state.copy()
        for row in range(num_rows):
            if curr_row < goal_row:
                # print("down")
                state_copy = self._move_down(state_copy, state_index)
                curr_row = self._get_row(state_copy, state_index + num_rows)
            elif curr_row > goal_row:
                # print("up")
                state_copy = self._move_up(state_copy, state_index)
                curr_row = self._get_row(state_copy, state_index - num_rows)
            else:
                break
            y_moves += 1
        return y_moves

    # euclidian distance = sqrt(x^2 + y^2), between a number's current location and it's goal location
    def _calculate_euclid_dist_hn(self, node):
        hn = 0.0
        node_state = node.get_state()
        goal_state = self.problem.get_goal_state()
        for index in range(len(node_state)): 
            # only calculate eudlicidan distance for the non empty spots
            if node_state[index] != 0:
                # if the num is not in the correct place, calculate euclidian distance
                if node_state[index] != goal_state[index]:
                    goal_index = goal_state.index(node_state[index])
                    x_moves = self._get_x_moves(node_state, goal_state, index, goal_index)
                    y_moves = self._get_y_moves(node_state, goal_state, index, goal_index)
                    euclid_dist = float(math.sqrt(x_moves ** 2 + y_moves ** 2))
                    hn += euclid_dist
                else:
                    pass
            else:
                pass
        return hn

    # calculate same gn for both heuristic functions
    # calculate different h(n)'s and according to user's choice of heuristic function
    # the corresponding h(n) will be added to f(n)
    def get_fn(self, node, root):
        gn = self.calculate_gn(node, root)
        node.set_gn(gn)
        hn = -1   
        if self.heuristic_choice == 2:
            hn = self.calculate_misplaced_tile_hn(node)
        else:
            hn = self._calculate_euclid_dist_hn(node)
            
        node.set_hn(hn)
        return node.get_gn() + node.get_hn() 

    # set node's heuristic value (fn) = g(n) + h(n)
    def set_heuristic(self, node):
        st_root = self._search_tree.get_root()
        fn = self.get_fn(node, st_root)
        node.set_heuristic_cost(fn)

    def solve_problem(self):
        self._init_frontier()
        while True:
            # if frontier is empty, return failure
            # if frontier.empty() == True:
            if len(self._frontier) == 0:
                return []
            else:
                
                # choose a leaf node and remove it from frontier
                self._update_max_nodes_in_frontier()
                
                # print nodes in frontier
                # for node in self._frontier:
                #     if node.get_parent() != None:
                #         print(node.get_state() , " dir: " , node.get_direction() ,", f(n) = ", str(node.get_heuristic_cost()))

                curr_node = self._frontier[0]
                self._frontier.pop(0)

                self.problem.print_node_info(curr_node)
                
                #print("curr_node from frontier : ", curr_node.get_state() , " dir: " , curr_node.get_direction())
                # if the node contains a goal state, then return the corresponding solution
                goal_state = self.problem.get_goal_state()
                if curr_node.is_goal_state(goal_state) == True:
                    self.expanded_nodes = len(self._explored) 
                    self.sol_depth = curr_node.get_depth()
                    return self._search_tree.get_solution_path(curr_node)
                else:
                    # add the node to the explored set
                    self._explored.append(curr_node)
                    # expand the chosen node
                    self.problem.expand_node(curr_node)
                    #  add the resulting nodes to the frontier
                    #     only if not in the frontier or explored set 
                    for child in curr_node.get_children():

                        self.set_heuristic(child)
                        

                        in_frontier = self._contains(self._frontier, child) 
                        in_explored = self._contains(self._explored, child)
                        if  (in_frontier == False) and (in_explored == False):


                            self._frontier.append(child)
                        else:
                            pass
                    # sort nodes in frontier by cost value 
                    self._frontier.sort(key=lambda x:x.get_heuristic_cost())
