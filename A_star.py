from problem import Problem
from tree import Tree
from node import Node


class A_star:
    def __init__(self, problem, h):
        self.problem = problem
        # 1 will be misplaced tile, # 2 will be euclidian dist
        self.heuristic = h  
        self._search_tree = None
        self._frontier = []
        self._explored = []

        self.num_expanded_nodes = 0
        self.max_nodes_in_frontier = 1
        self.sol_depth = 0


    def get_heuristic(self):
        return self.heuristic

    def set_heuristic(self, h):
        self.heuristic = h
        # if 1--> tiles
        # if 2 --> dist 
        # calculate heuristic in a star algo not in node ...

    def get_num_exanded_nodes(self):
        return self.num_expanded_nodes

    def get_max_nodes_in_frontier(self):
        return self.max_nodes_in_frontier
    
    def get_sol_depth(self):
        return self.sol_depth

    def _init_frontier(self):
        init_state = self.problem.get_init_state()
        root = Node(init_state)
        root.set_path_cost(0)
        self._search_tree = Tree(root)
        self.problem.set_search_tree(self._search_tree)  ## change this, so A star finds this 
        self._frontier.append(root)

    def _contains(self, iterable, child):
        for node in iterable:
            if node.get_state() == child.get_state():
                return True
            else:
                pass
        return False

    def solve_problem(self):
        self._init_frontier()
        while True:
            # if frontier is empty, return failure
            # if frontier.empty() == True:
            if len(self._frontier) == 0:
                print("here")
                return []
            else:
                # choose a leaf node and remove it from frontier
                nodes_in_frontier = len(self._frontier)
                if nodes_in_frontier > self.max_nodes_in_frontier:
                    self.max_nodes_in_frontier = nodes_in_frontier
                else:
                    pass
                
                # print nodes in frontier
                for node in self._frontier:
                    if node.get_parent() != None:
                        print(node.get_state() , " dir: " , node.get_direction() ,", f(n) = ", str(node.get_heuristic_cost()))

                curr_node = self._frontier[0]
                self._frontier.pop(0)
                
                print("curr_node from frontier : ", curr_node.get_state() , " dir: " , curr_node.get_direction())
                # if the node contains a goal state, then return the corresponding solution
                
                if self.problem.is_goal_state(curr_node) == True:
                    self.expanded_nodes = len(self._explored) 
                    self.sol_depth = curr_node.get_depth()
                    info = [self.expanded_nodes, self.max_nodes_in_frontier, self.sol_depth]

                    return self.problem.get_solution_path(curr_node)
                else:
                    # add the node to the explored set
                    self._explored.append(curr_node)
                    # expand the chosen node, adding the resulting nodes to the frontier
                    #     only if not in the frontier or explored set 
                    self.problem.expand_node(curr_node)

                    for child in curr_node.get_children():
                        # print(child.get_direction())
                        # problem.print_state(child)
                        # print()

                        in_frontier = self._contains(self._frontier, child) 
                        in_explored = self._contains(self._explored, child)
                        # print(in_frontier , in_explored)
                        if  (in_frontier == False) and (in_explored == False):
                            self._frontier.append(child)
                            # print("added " + child.get_direction())
                        else:
                            pass
                            # print("NOT added " + child.get_direction())

                    # sort nodes in frontier by cost value 
                    self._frontier.sort(key=lambda x:x.get_heuristic_cost())

