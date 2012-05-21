# -----------------
# User Instructions
# 
# In this problem you will be refactoring the bsuccessors function.
# Your new function, bsuccessors3, will take a state as an input
# and return a dict of {state:action} pairs. 
#
# A state is a (here, there, light) tuple. Here and there are 
# frozensets of people (each person is represented by an integer
# which corresponds to their travel time), and light is 0 if 
# it is on the `here` side and 1 if it is on the `there` side.
#
# An action is a tuple of (travelers, arrow), where the arrow is
# '->' or '<-'. See the test() function below for some examples
# of what your function's input and output should look like.

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

def bsuccessors3(state):
    """Return a dict of {state:action} pairs.  State is (here, there, light)
    where here and there are frozen sets of people, light is 0 if the light is 
    on the here side and 1 if it is on the there side.
    Action is a tuple (travelers, arrow) where arrow is '->' or '<-'"""
    here, there, light = state
    import itertools 
    result = {}
    if light == 0:
        action='->'
        light=1
        for persons in itertools.product(here, repeat=2):
            cross=frozenset(persons)
            a,b = persons
            result[(here-cross,there|cross,light)] = (cross, '->')
    elif light == 1:
        action='<-'
        light=0
        for persons in itertools.product(there, repeat=2):
            cross=frozenset(persons)
            a,b = persons
            result[(here|cross,there-cross,light)] = (cross, '<-')
    # your code here  
    return result



def test():
    assert bsuccessors3((frozenset([1]), frozenset([]), 0)) == {
            (frozenset([]), frozenset([1]), 1)  :  (set([1]), '->')}

    assert bsuccessors3((frozenset([1, 2]), frozenset([]), 0)) == {
            (frozenset([1]), frozenset([2]), 1)    :  (set([2]), '->'), 
            (frozenset([]), frozenset([1, 2]), 1)  :  (set([1, 2]), '->'), 
            (frozenset([2]), frozenset([1]), 1)    :  (set([1]), '->')}

    assert bsuccessors3((frozenset([2, 4]), frozenset([3, 5]), 1)) == {
            (frozenset([2, 4, 5]), frozenset([3]), 0)   :  (set([5]), '<-'), 
            (frozenset([2, 3, 4, 5]), frozenset([]), 0) :  (set([3, 5]), '<-'), 
            (frozenset([2, 3, 4]), frozenset([5]), 0)   :  (set([3]), '<-')}
    return 'tests pass'

print test()
dit = bsuccessors3((frozenset([1]), frozenset([]), 0))
for key in dit:
    print key
    print dit[key]
dit = bsuccessors3((frozenset([2, 4]), frozenset([3, 5]), 1))

for key in dit:
    print key
    print dit[key]
