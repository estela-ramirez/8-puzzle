from uniform_search import uniform_cost_search

if __name__ == "__main__":
    solution = uniform_cost_search("problem")
    if  solution == []:
        print("Failure")
    else:
        print(solution)
   