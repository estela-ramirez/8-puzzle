from multiprocessing.sharedctypes import Value
from problem import Problem
from uniform_search import uniform_cost_search
from A_star import A_star

# asks user for puzzle option 
# return (1) default, (2) their own
def get_puzzle_option():
    puzzle_option = input()
    
    while True:
        try:
            puzzle_option = int(puzzle_option)
            if (puzzle_option != 1) and (puzzle_option != 2):
                raise ValueError
            else:
                break
        except ValueError:
            puzzle_option = input("Enter \"1\" or \"2\": ")
    return puzzle_option

# if the user entered option (2), ask them for their puzzle layout
# return puzzle initial state, []
def get_user_puzzle(puzzle_option):
    # could add more error checking
    def_puzzle = [1, 2, 3, 4, 5, 6, 7, 0, 8]
    if puzzle_option == 2:
        try:
            print("Enter your puzzle, use a zero to represent the blank")
            print("Enter the first row, use space or tabs between numbers")
            first_row = input().split()
            print("Enter the second row, use space or tabs between numbers")
            second_row = input().split()
            print("Enter the third row, use space or tabs between numbers")
            third_row = input().split()
            puzzle = first_row + second_row + third_row
            for num in range(len(puzzle)):
                puzzle[num] = int(puzzle[num])
            return puzzle
        except Exception:
            print("Invalid puzzle. Will use default")
            return def_puzzle 
    else:
        pass
    return def_puzzle

#return algo choice, int 
# (1) UCS
# (2) A* with misplaced tile heuristic
# (3) A* with Eudlidian distance heuristic
def get_algo_choice():
    print("Enter your choice of algorithm")
    print("(1) Uniform Cost Search")
    print("(2) A* with Mispalced Tile Heuristic")
    print("(3) A* with the Euclidian distance Heuristic")

    choice = input()
    while True:
        try:
            choice = int(choice)
            if choice != 1 and choice != 2 and choice != 3:
                raise ValueError
            else:
                break
        except ValueError:
            print("Enter 1, 2, or 3")
            choice = input()

    return choice


def get_sol_from_algo(algo_choice, problem):
    path = []
    info = [0, 0, 0]  
    if algo_choice == 1:
        path, info = uniform_cost_search(problem)
    elif algo_choice == 2:
         A_star_MT = A_star(problem, 2)
         path = A_star_MT.solve_problem() 
         info = [A_star_MT.get_num_exanded_nodes(), A_star_MT.get_max_nodes_in_frontier(), A_star_MT.get_sol_depth()]
    else:
        A_star_ED = A_star(problem, 3)
        path = A_star_ED.solve_problem() 
        info = [A_star_ED.get_num_exanded_nodes(), A_star_ED.get_max_nodes_in_frontier(), A_star_ED.get_sol_depth()]
    return (path, info)

if __name__ == "__main__":
    puzzle_cols = 3
    print("Welcome to 861293832 8 puzzle solver.")
    print("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle: ")

    puzzle_option = get_puzzle_option()
    puzzle = get_user_puzzle(puzzle_option)
    problem = Problem(puzzle_cols, puzzle)

    # problem1 = Problem(puzzle_cols, [1, 2, 3, 4, 5, 6, 7, 8, 0])
    # problem2 = Problem(puzzle_cols, [1, 2, 3, 4, 5, 6, 7, 0, 8])
    # problem3 = Problem(puzzle_cols, [1, 2, 0, 4, 5, 3, 7, 8, 6])  
    # problem4 = Problem(puzzle_cols, [0, 1, 2, 4, 5, 3, 7, 8, 6])
    # problem5 = Problem(puzzle_cols, [8, 7, 1, 6, 0, 2, 5, 4, 3])  
    # problem6 = Problem(puzzle_cols, [1, 2, 3, 4, 5, 6, 8, 7, 0])

    algo_choice = get_algo_choice()
    path, info = get_sol_from_algo(algo_choice, problem)
    
    # testing 
    # A_star_euclid = A_star(problem1, 2)
    # path = A_star_euclid.solve_problem()
    # info = [A_star_euclid.get_num_exanded_nodes(), A_star_euclid.get_max_nodes_in_frontier(), A_star_euclid.get_sol_depth()]
    # testing

    if  path == []:
        print("No path")
    else:
        print("\nGoal!!!\n")
        print("\nTo solve this problem the algorithm expanded a total of {0} nodes.".format(info[0]))
        print("The maximum number of nodes in the queue at any one time: {0}".format(info[1]))
        print("the depth of the goal node was {0}\n".format(info[2]))
        
        print("Printing solution path ... ")
        problem.print_solution_path(path) 
        


