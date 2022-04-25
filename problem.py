class Problem:
    def __init__(self, init_state = [1, 9, 3, 4, 2, 6, 7, 5, 8]):
        self.init_state = init_state
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # operators for the blank space (*), if there is a number in that direction
        self.operators = ['left', 'right', 'up', 'down']

