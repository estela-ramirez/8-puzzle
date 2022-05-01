from problem import Problem
from tree import Tree
from node import Node


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

    def calculate_euclid_dist_hn(self, node):
        hn = 0
        
        return hn

    def get_fn(self, node, root):
        gn = self.calculate_gn(node, root)
        node.set_gn(gn)
        hn = -1   
        if self.heuristic_choice == 2:
            hn = self.calculate_misplaced_tile_hn(node)
        else:
            hn = self.calculate_euclid_dist_hn(node)
        
        node.set_hn(hn)
        print("choice = ", self.heuristic_choice, " ******* gn = ", node.get_gn(), "hn = ", node.get_hn())
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
                
                if len(self._explored) > 2400:
                    return []
                # print nodes in frontier
                for node in self._frontier:
                    if node.get_parent() != None:
                        print(node.get_state() , " dir: " , node.get_direction() ,", f(n) = ", str(node.get_heuristic_cost()))

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