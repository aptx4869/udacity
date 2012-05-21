# -----------------
# User Instructions
# 
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are 
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is 
# '->' for here to there or '<-' for there to here. When only one 
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
    '<-' for there to here."""
    here, there, t = state
    import itertools 
    result = {}
    if 'light' in here:
        persons_here = here-set(['light'])
        for persons in itertools.product(persons_here, repeat=2):
            cross=frozenset(persons)|frozenset(['light'])
            a,b = persons
            result[(here-cross,there|cross,t+max(persons))] = (a,b, '->')
    elif 'light' in there:
        persons_there = there-set(['light'])
        for persons in itertools.product(persons_there, repeat=2):
            cross=frozenset(persons)|frozenset(['light'])
            a,b = persons
            result[(here|cross,there-cross,t+max(persons))] = (a,b, '<-')
    # your code here  
    return result

    #return {((0, y+x) if y+x <= Y else (x-(Y-y), y+(Y-y))): 'X->Y',
             #((x+y, 0) if x+y <= X else (x+(X-x), y-(X-x))): 'X<-Y',
             #(X, y): 'fill X',
             #(x, Y): 'fill Y',
             #(0, y): 'empty X',
             #(x, 0): 'empty Y'
             #}


def test():

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
    
    return 'tests pass'

print test()


print bsuccessors((frozenset([1, 'light']), frozenset([]), 3))
