# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

def successors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    state = list(state)
    result={}

    def inbondary(state,grid):
        return 0 <=state[0] < len(grid) and 0 <= state[1] < len(grid[0])

    def newstate(state, movement):
        state1=[state[i]+movement[i] for i in range(len(state))]
        return state1 if inbondary(state1,grid) else None


    for i in range(len(delta)):
        state1=newstate(state,delta[i])
        if state1:
            if grid[state1[0]][state1[1]]!=1:
                result[tuple(state1)] = delta_name[i]
    return result
    
def is_goal(state):
    return list(state) == goal

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set()
    frontier = [ [start] ] 
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return Fail
Fail = []

def lowest_cost_search(start, successors, is_goal, action_cost):
    """Return the lowest cost path, starting from start state,
    and considering successors(state) => {state:action,...},
    that ends in a state for which is_goal(state) is true,
    where the cost of a path is the sum of action costs,
    which are given by action_cost(action)."""
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    def final_state(path):
        return path[-1]
    def path_cost(path):
        if len(path) < 3:
            return 0
        else:
            action, total_cost = path[-2]
            return total_cost

    while frontier:
        path = frontier.pop(0)
        state1 = final_state(path)
        if is_goal(state1):  
            return path
        explored.add(state1)
        pcost = path_cost(path)
        for (state, action) in successors(state1).items():
            if state not in explored:
                total_cost = pcost + action_cost(action)
                path2 = path + [(action, total_cost), state]
                frontier.append(path2)
                #add_to_frontier(frontier, path2)
    return Fail


delta_name = ['^', '<', 'v', '>']

cost = 1
def search():
    start=tuple(init)
    def action_cost(action):
        return cost
    path=lowest_cost_search(start, successors, is_goal, action_cost)
    if len(path) < 3:
        if not path:
            return 'fail'
        return [0,path[0][0],path[0][1]]
    else:
        result=path[-2:]
        return [result[0][1], result[1][0],result[1][1]]

    
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------


print search()
