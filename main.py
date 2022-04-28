from multiprocessing.sharedctypes import Value
from problem import Problem
from uniform_search import uniform_cost_search
from A_star_Mispl_Tile import A_star_Misplaced_Tile
from A_star_Eucl_dist import A_star_Euclidian_Dist

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
    info = []  
    print(algo_choice)
    if algo_choice == 1:
        print("chose UCS")
        path, info = uniform_cost_search(problem)
    elif algo_choice == 2:
        print("chose Misplaced Tile")
        path, info = A_star_Misplaced_Tile(problem)
    else:
        print("chose Euc Dist")
        path, info = A_star_Euclidian_Dist(problem)
    return (path, info)

if __name__ == "__main__":
    puzzle_cols = 3
    print("Welcome to 861293832 8 puzzle solver.")
    print("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle: ")

    puzzle_option = get_puzzle_option()
    puzzle = get_user_puzzle(puzzle_option)
    problem = Problem(puzzle_cols, puzzle)

    # problem5 = Problem(puzzle_cols, [1, 2, 3, 4, 5, 6, 7, 8, 0])
    # problem1 = Problem(puzzle_cols, [1, 2, 3, 4, 5, 6, 7, 0, 8])  
    # problem2 = Problem(puzzle_cols, [1, 2, 3, 4, 5, 0, 7, 8, 6])  
    # problem3 = Problem(puzzle_cols, [1, 2, 3, 4, 8, 0, 7, 6, 5])
    # problem4 = Problem(puzzle_cols, [1, 0, 3, 4, 2, 6, 7, 5, 8])

    algo_choice = get_algo_choice()
    path, info = get_sol_from_algo(algo_choice, problem)

    if  path == []:
        print("No path")
    else:
        problem.print_solution_path(path)
        print("Goal!!!\n")

        print("To solve this problem the algorithm expanded a total of {0} nodes.".format(info[0]))
        print("The maximum number of nodes in the queue at any one time: {0}".format(info[1]))
        print("the depth of the goal node was {0}\n".format(info[2]))