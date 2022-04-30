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

def calculate_gn(node, root):
    gn = 0
    gn += node.get_path_cost()

    while (node.get_parent() != None):
        node = node.get_parent()
        gn += node.get_path_cost()
    return gn

def uniform_cost_search(problem):
    # intialize frontier using initial state of problem
    init_state = problem.get_init_state()
    root = Node(init_state)
    search_tree = Tree(root)
    
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

            curr_node = frontier[0]
            frontier.pop(0)
            
            # print("curr_node from frontier : ", curr_node.get_state() , " dir: " , curr_node.get_direction())
            # if the node contains a goal state, then return the corresponding solution
            goal_state = problem.get_goal_state()
            if curr_node.is_goal_state(goal_state) == True:
                expanded_nodes = len(explored) 
                sol_depth = curr_node.get_depth()
                info = [expanded_nodes, max_nodes_in_frontier, sol_depth]

                return (search_tree.get_solution_path(curr_node), info)
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

                    st_root = search_tree.get_root()
                    gn = calculate_gn(child, st_root)
                    child.set_gn(gn)
                    child.set_heuristic_cost(gn)

                    in_frontier = contains(frontier, child) 
                    in_explored = contains(explored, child)
                    # print(in_frontier , in_explored)
                    if  (in_frontier == False) and (in_explored == False):
                        frontier.append(child)
                        # print("added " + child.get_direction())
                    else:
                        pass
                        # print("NOT added " + child.get_direction())
