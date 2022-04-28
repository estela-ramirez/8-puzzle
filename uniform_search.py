from problem import Problem
from tree import Tree
from node import Node
from queue import PriorityQueue

def contains(iterable, child):
    for node in iterable:
        if node.get_state() == child.get_state():
            return True
        else:
            pass
    return False

        
def uniform_cost_search(problem):
    # intialize frontier using initial state of problem
    init_state = problem.get_init_state()
    root = Node(init_state)
    tr = Tree(root)
    
    #pq = PriorityQueue()
    pq = []
    #pq.put(root)
    pq.append(root)

    # intialized explored list to empty
    explored = []
    
    count  = 0
    while True:
        # if frontier is empty, return failure
        # if pq.empty() == True:
        if len(pq) == 0:
            return []
        else:
            # choose a leaf node and remove it from frontier
            #curr_node = pq.get()

            print("printing frontier ...")
            print("nodes in frontier = ", len(pq))
            for node in pq:
                print(node)

            curr_node = pq[0]
            pq.pop(0)
            
            
            print("curr_node from frontier : ", curr_node.get_state() , " dir: " , curr_node.get_direction())
            # if the node contains a goal state, then return the corresponding solution
            if problem.is_goal_state(curr_node) == True:
                print("Done!!!")
                return problem.get_solution_path(curr_node)
            else:
                # add the node to the explored set
                explored.append(curr_node)
                # expand the chosen node, adding the resulting nodes to the frontier
                #     only if not in the frontier or explored set 
                problem.expand_node(curr_node)

                for child in curr_node.get_children():
                    print(child.get_direction())
                    problem.print_state(child)
                    print()

                    in_frontier = contains(pq, child) 
                    in_explored = contains(explored, child)
                    print(in_frontier , in_explored)
                    if  (in_frontier == False) and (in_explored == False):
                        #pq.put(child)
                        pq.append(child)
                        print("added " + child.get_direction())
                    else:
                        print("NOT added " + child.get_direction())
                # if count == 4:
                #     return []

        count+=1