from problem import Problem
from tree import Tree
from node import Node

def contains(iterable, child):
    for node in iterable:
        if node.get_state() == child.get_state():
            return True
        else:
            pass
    return False

def A_star_Misplaced_Tile(problem):
    # intialize frontier using initial state of problem
    init_state = problem.get_init_state()
    root = Node(init_state)
    root.set_path_cost(0)
    tr = Tree(root)
    problem.set_search_tree(tr)
    
    frontier = []
    frontier.append(root)
    max_nodes_in_frontier = 1

    # intialized explored set/list to empty
    explored = []
    
    while True:
        # if frontier is empty, return failure
        # if frontier.empty() == True:
        if len(frontier) == 0:
            return []
        else:
            # choose a leaf node and remove it from frontier
            nodes_in_frontier = len(frontier)
            if nodes_in_frontier > max_nodes_in_frontier:
                max_nodes_in_frontier = nodes_in_frontier
            else:
                pass
            
            # print nodes in frontier
            for node in frontier:
                if node.get_parent() != None:
                    print(node.get_state() , " dir: " , node.get_direction() ,", f(n) = ", str(node.get_heuristic_cost()))

            curr_node = frontier[0]
            frontier.pop(0)
            
            print("curr_node from frontier : ", curr_node.get_state() , " dir: " , curr_node.get_direction())
            # if the node contains a goal state, then return the corresponding solution
            
            if problem.is_goal_state(curr_node) == True:
                expanded_nodes = len(explored) 
                sol_depth = curr_node.get_depth()
                info = [expanded_nodes, max_nodes_in_frontier, sol_depth]

                return (problem.get_solution_path(curr_node), info)
            else:
                # add the node to the explored set
                explored.append(curr_node)
                # expand the chosen node, adding the resulting nodes to the frontier
                #     only if not in the frontier or explored set 
                problem.expand_node(curr_node)

                for child in curr_node.get_children():
                    # print(child.get_direction())
                    # problem.print_state(child)
                    # print()

                    in_frontier = contains(frontier, child) 
                    in_explored = contains(explored, child)
                    # print(in_frontier , in_explored)
                    if  (in_frontier == False) and (in_explored == False):
                        frontier.append(child)
                        # print("added " + child.get_direction())
                    else:
                        pass
                        # print("NOT added " + child.get_direction())

                # sort nodes in frontier by cost value 
                frontier.sort(key=lambda x:x.get_heuristic_cost())