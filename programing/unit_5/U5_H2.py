# -----------------
# User Instructions
# 
# In this problem, we introduce doubling to the game of pig. 
# At any point in the game, a player (let's say player A) can
# offer to 'double' the game. Player B then has to decide to 
# 'accept', in which case the game is played through as normal,
# but it is now worth two points, or 'decline,' in which case
# player B immediately loses and player A wins one point. 
#
# Your job is to write two functions. The first, pig_actions_d,
# takes a state (p, me, you, pending, double), as input and 
# returns all of the legal actions.
# 
# The second, strategy_d, is a strategy function which takes a
# state as input and returns one of the possible actions. This
# strategy needs to beat hold_20_d in order for you to be
# marked correct. Happy pigging!

import random
from functools import update_wrapper

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def trace(f):
    indent = '   '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print '%s--> %s' % (trace.level*indent, signature)
        trace.level += 1
        try:
            result=f(*args)
            # your code here
            print '%s<-- %s == %s' % ((trace.level-1)*indent, 
                                      signature, result)
        finally:
            trace.level -=1
            #pass
            # your code here
        return result# your code here
    trace.level = 0
    return _f

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args refuses to be a dict key
            return f(args)
    _f.cache = cache
    return _f

def pig_actions_d(state):
    """The legal actions from a state. Usually, ["roll", "hold"].
    Exceptions: If double is "double", can only "accept" or "decline".
    Can't "hold" if pending is 0.
    If double is 1, can "double" (in addition to other moves).
    (If double > 1, cannot "double").
    """
    # state is like before, but with one more component, double,
    # which is 1 or 2 to denote the value of the game, or 'double'
    # for the moment at which one player has doubled and is waiting
    # for the other to accept or decline
    (p, me, you, pending, double) = state 
    # your code here
    if double == "double":
        return ["accept", "decline"]
    elif double == 1:
        return ["roll", "hold", "double"] if pending>0 else ["roll", "double"]
    elif double >1:
        return ["roll", "hold"] if pending>0 else ["roll"]

@memo
def strategy_d(state):
    def di(i):
        while True:
            yield i

    def Q_pig(state, action, Pwin):  
        "The expected value of choosing action in state."
        if action == 'decline':
            return 0
        if action == 'roll':
            return (1 - P_H20(do('roll',state, di(1)))
                    + sum(Pwin(do('roll',state, d))
                        for d in (di(i) for i in range(2,7)))) / 6.
        if action == 'hold':
            return 1 - P_H20(do('hold', state,dierolls))
        if action == 'double':
            return P_H20(do('double', state,dierolls))
        if action == 'accept':
            return P_H20(do('accept', state,dierolls))
        raise ValueError

    def P_H20(state):
        (p, me, you, pending, double) = state 
        if me + pending >= goal:
            return 1
        elif you >= goal:
            return 0
        elif me + pending >=20:
            return 1 - Pwin(do('hold',state, di(1)))
        else:
            return (1 - Pwin(do('roll',state, di(1)))
                    + sum(P_H20(do('roll',state, d))
                        for d in (di(i) for i in range(2,7)))) / 6.
            #return max(Q_pig((0,me,you,pending,double), action, Pwin)

    def Pwin(state):
        """The utility of a state; here just the probability that an optimal player
        whose turn it is to move can win from the current state."""
        # Assumes opponent also plays with optimal strategy.
        (p, me, you, pending, double) = state 
        return Pwin3(me, you, pending,double)
        
    @trace
    @memo
    def Pwin3(me, you, pending,double):
        if me + pending >= goal:
            return 1
        elif you >= goal:
            return 0
        else:
            return max(Q_pig((0,me,you,pending,double), action, Pwin)
                       for action in pig_actions_d((0,me,you,pending,double)) if action != 'decline')

    @memo
    def best_action(state, actions, Q, U):
        "Return the optimal action for a state, given U."
        def EU(action): return Q(state, action, U)
        return max(actions(state), key=EU)
    
    return best_action(state, pig_actions_d, Q_pig, Pwin)
    # your code here


## You can use the code below, but don't need to modify it.

def hold_20_d(state):
    "Hold at 20 pending.  Always accept; never double."
    (p, me, you, pending, double) = state
    return ('accept' if double == 'double' else
            'hold' if (pending >= 20 or me + pending >= goal) else
            'roll')
    
def double_20_d(state):
    "Hold at 20 pending.  Always accept; never double."
    (p, me, you, pending, double) = state
    return ('accept' if double == 'double' else 
            'hold' if (me + pending >= goal and double !=1) else 
            'double' if (double ==1 and me + pending >= goal) else 'roll')

def clueless_d(state):
    return random.choice(pig_actions_d(state))
 
def dierolls():
    "Generate die rolls."
    while True:
        yield random.randint(1, 6)

def play_pig_d(A, B, dierolls=dierolls()):
    """Play a game of pig between two players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player."""
    strategies = [A, B]
    state = (0, 0, 0, 0, 1)
    while True:
        (p, me, you, pending, double) = state
        if me >= goal:
            return strategies[p], double
        elif you >= goal:
            return strategies[other[p]], double
        else:
            action = strategies[p](state)
            state = do(action, state, dierolls)

## No more roll() and hold(); instead, do:

def do(action, state, dierolls):
    """Return the state that results from doing action in state.
     If action is not legal, return a state where the opponent wins.
    Can use dierolls if needed."""
    (p, me, you, pending, double) = state
    if action not in pig_actions_d(state):
        return (other[p], goal, 0, 0, double)
    elif action == 'roll':
        d = next(dierolls)
        if d == 1:
            return (other[p], you, me+1, 0, double) # pig out; other player's turn
        else:
            return (p, me, you, pending+d, double)  # accumulate die in pending
    elif action == 'hold':
        return (other[p], you, me+pending, 0, double)
    elif action == 'double':
        return (other[p], you, me, pending, 'double')
    elif action == 'decline':
        return (other[p], goal, 0, 0, 1)
    elif action == 'accept':
        return (other[p], you, me, pending, 2)

goal = 40
other = {1:0, 0:1}

def strategy_compare(A, B, N=1000):
    """Takes two strategies, A and B, as input and returns the percentage
    of points won by strategy A."""
    A_points, B_points = 0, 0
    for i in range(N):
        if i % 2 == 0:  # take turns with who goes first
            winner, points = play_pig_d(A, B)
        else: 
            winner, points = play_pig_d(B, A)
        if winner.__name__ == A.__name__:
            A_points += points
        else: B_points += points
    A_percent = 100*A_points / float(A_points + B_points)
    print 'In %s games of pig, strategy %s took %s percent of the points against %s.' % (N, A.__name__, A_percent, B.__name__)
    return A_percent
    
def test():
    assert set(pig_actions_d((0, 2, 3, 0, 1)))          == set(['roll', 'double'])
    assert set(pig_actions_d((1, 20, 30, 5, 2)))        == set(['hold', 'roll']) 
    assert set(pig_actions_d((0, 5, 5, 5, 1)))          == set(['roll', 'hold', 'double'])
    assert set(pig_actions_d((1, 10, 15, 6, 'double'))) == set(['accept', 'decline']) 
    assert strategy_compare(strategy_d, hold_20_d) > 60 # must win 60% of the points      
    return 'test passes'

#print test()
print strategy_compare(double_20_d, hold_20_d)



