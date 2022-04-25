from problem import Problem
from queue import PriorityQueue

def uniform_cost_search(problem):
    # intialize frontier using initial state of problem
    pq = PriorityQueue()

    # pq.put()
    # intialized explored set to empty
    explored = set()
    
    while True:
        # if frontier is empty, return failure
        if pq.empty() == True:
            return []
        else:
            pass

            # choose a leaf node and remove it from frontier
            # if the node contains a goal state, then return the corresponding solution
            # add the node to the explored set
            # expand the chosen node, adding the resulting nodes to the frontier
                # only if not in the frontier or explored set 
