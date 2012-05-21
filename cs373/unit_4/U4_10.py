# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. NOTE: the 'v' should be 
# lowercase.
#
# Your function should be able to do this for any
# provided grid, not just the sample grid below.
# ----------


# Sample Test case
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

# ----------------------------------------
# modify code below
# ----------------------------------------
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

def search():
    start=tuple(init)
    result = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    
    def action_cost(action):
        return cost

    def g_2int(l):
        N=len(l)
        for i in range(0,N-1,2):
            yield i,i+1

    path=lowest_cost_search(start, successors, is_goal, action_cost)

    for i,j in g_2int(path):
        result[path[i][0]][path[i][1]]= path[j][0]
    result[goal[0]][goal[1]]='*'

    return result





print search()
