import doctest

# -----------------
# User Instructions
# 
# In this problem, you will solve the pouring problem for an arbitrary
# number of glasses. Write a function, more_pour_problem, that takes 
# as input capacities, goal, and (optionally) start. This function should 
# return a path of states and actions.
#
# Capacities is a tuple of numbers, where each number represents the 
# volume of a glass. 
#
# Goal is the desired volume and start is a tuple of the starting levels
# in each glass. Start defaults to None (all glasses empty).
#
# The returned path should look like [state, action, state, action, ... ]
# where state is a tuple of volumes and action is one of ('fill', i), 
# ('empty', i), ('pour', i, j) where i and j are indices indicating the 
# glass number. 



def more_pour_problem(capacities, goal, start=None):
    """The first argument is a tuple of capacities (numbers) of glasses; the
    goal is a number which we must achieve in some glass.  start is a tuple
    of starting levels for each glass; if None, that means 0 for all.
    Start at start state and follow successors until we reach the goal.
    Keep track of frontier and previously explored; fail when no frontier.
    On success return a path: a [state, action, state2, ...] list, where an
    action is one of ('fill', i), ('empty', i), ('pour', i, j), where
    i and j are indices indicating the glass number."""

    N=len(capacities)
    start  = tuple(0 for _ in range(N)) if start == None else start

    def successors(capacities):
        def _s(state):
            assert len(state) == N
            import itertools 
            result={}
            list_state=list(state)
            for index_x,index_y in itertools.product(range(N),range(N)):
                capacity_x=capacities[index_x]
                capacity_y=capacities[index_y]
                state_x=list_state[index_x]
                state_y=list_state[index_y]
                result_state=list_state[:]
                if index_x == index_y:
                    if state_x!=0:
                        result_state[index_x]=0
                        result[tuple(result_state)]=('empty',index_x)
                    if state_x!=capacity_x:
                        result_state[index_x]=capacity_x
                        result[tuple(result_state)]=('fill',index_x)

                elif state_x!=0 and state_y!=capacity_y:
                    #in else case, index != index_y, so check for pouring
                    if state_x + state_y < capacity_y:
                        result_state[index_x]=0
                        result_state[index_y]=state_x + state_y
                    else:
                        result_state[index_x]=state_x-capacity_y+state_y
                        result_state[index_y]=capacity_y
                    result[tuple(result_state)]=('pour', index_x, index_y)

            return result
        return _s


    def is_goal(goal):
        def _g(g):
            return True if goal in g else False
        return _g

    return shortest_path_search(start, successors(capacities), is_goal(goal)) 

    

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
    
def test_more_pour():
    assert more_pour_problem((1, 2, 4, 8), 4) == [
        (0, 0, 0, 0), ('fill', 2), (0, 0, 4, 0)]
    assert more_pour_problem((1, 2, 4), 3) == [
        (0, 0, 0), ('fill', 2), (0, 0, 4), ('pour', 2, 0), (1, 0, 3)] 
    starbucks = (8, 12, 16, 20, 24)
    assert not any(more_pour_problem(starbucks, odd) for odd in (3, 5, 7, 9))
    assert all(more_pour_problem((1, 3, 9, 27), n) for n in range(28))
    assert more_pour_problem((1, 3, 9, 27), 28) == []
    return 'test_more_pour passes'

print test_more_pour()

############################################
#def pour_problem(X, Y, goal, start = (0, 0)):
    #"""X and Y are the capacity of glasses; (x,y) is current fill levels and
    #represent a state. The goal is a level that can be in either glass. Start at
    #start state and follow successors until we reach the goal. Keep track of
    #frontier and previously explored; fail when no frontier."""
    #if goal in start:
        #return [start]
    #explored = set() # set the states we have visited
    #frontier = [ [start] ] # ordered list of paths we have blazed
    #while frontier:
        #path = frontier.pop(0)
        #(x, y) = path[-1] # Last state in the first path of the frontier
        #for (state, action) in successors(x, y, X, Y).items():
            #if state not in explored:
                #explored.add(state)
                #path2 = path + [action, state]
                #if goal in state:
                    #return path2
                #else:
                    #frontier.append(path2)
    #return Fail
#Fail = []

#def successors(x, y, X, Y):
    #"""Return a dict of {state:action} pairs describing what can be reached from
    #the (x, y) state and how."""
    #assert x <= X and y <= Y ## (x, y) is glass levels; X and Y are glass sizes
    #return {((0, y+x) if y+x <= Y else (x-(Y-y), y+(Y-y))): 'X->Y',
            #((x+y, 0) if x+y <= X else (x+(X-x), y-(X-x))): 'X<-Y',
            #(X, y): 'fill X',
            #(x, Y): 'fill Y',
            #(0, y): 'empty X',
            #(x, 0): 'empty Y'
            #}

#class Test:
    #"""
    #>>> successors(0, 0, 4, 9)
    #{(0, 9): 'fill Y', (0, 0): 'empty Y', (4, 0): 'fill X'}

    #>>> successors(3, 5, 4, 9)
    #{(4, 5): 'fill X', (4, 4): 'X<-Y', (3, 0): 'empty Y', (3, 9): 'fill Y', (0, 5): 'empty X', (0, 8): 'X->Y'}

    #>>> successors(3, 7, 4, 9)
    #{(4, 7): 'fill X', (4, 6): 'X<-Y', (3, 0): 'empty Y', (0, 7): 'empty X', (3, 9): 'fill Y', (1, 9): 'X->Y'}

    #>>> pour_problem(4, 9, 6)
    #[(0, 0), 'fill Y', (0, 9), 'X<-Y', (4, 5), 'empty X', (0, 5), 'X<-Y', (4, 1), 'empty X', (0, 1), 'X<-Y', (1, 0), 'fill Y', (1, 9), 'X<-Y', (4, 6)]

    ### What problem, with X, Y, and goal < 10 has the longest solution?
    ### Answer: pour_problem(7, 9, 8) with 14 steps.

    #>>> def num_actions(triplet): X, Y, goal = triplet; return len(pour_problem(X, Y, goal)) / 2

    #>>> def hardness(triplet): X, Y, goal = triplet; return num_actions((X, Y, goal)) - max(X, Y)
    #>>> max([(X, Y, goal) for X in range(1, 10) for Y in range(1, 10)
    #...                   for goal in range(1, max(X, Y))], key = num_actions)
    #(7, 9, 8)

    #>>> max([(X, Y, goal) for X in range(1, 10) for Y in range(1, 10)
    #...                   for goal in range(1, max(X, Y))], key = hardness)
    #(7, 9, 8)

    #>>> pour_problem(7, 9, 8)
    #[(0, 0), 'fill Y', (0, 9), 'X<-Y', (7, 2), 'empty X', (0, 2), 'X<-Y', (2, 0), 'fill Y', (2, 9), 'X<-Y', (7, 4), 'empty X', (0, 4), 'X<-Y', (4, 0), 'fill Y', (4, 9), 'X<-Y', (7, 6), 'empty X', (0, 6), 'X<-Y', (6, 0), 'fill Y', (6, 9), 'X<-Y', (7, 8)]
    #"""

#print(doctest.testmod())
## TestResults(failed=0, attempted=9)


