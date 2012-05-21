# -----------------
# User Instructions
# 
# This problem deals with the one-player game foxes_and_hens. This 
# game is played with a deck of cards in which each card is labelled
# as a hen 'H', or a fox 'F'. 
# 
# A player will flip over a random card. If that card is a hen, it is
# added to the yard. If it is a fox, all of the hens currently in the
# yard are removed.
#
# Before drawing a card, the player has the choice of two actions, 
# 'gather' or 'wait'. If the player gathers, she collects all the hens
# in the yard and adds them to her score. The drawn card is discarded.
# If the player waits, she sees the next card. 
#
# Your job is to define two functions. The first is do(action, state), 
# where action is either 'gather' or 'wait' and state is a tuple of 
# (score, yard, cards). This function should return a new state with 
# one less card and the yard and score properly updated.
#
# The second function you define, strategy(state), should return an 
# action based on the state. This strategy should average at least 
# 1.5 more points than the take5 strategy.

import random
from functools import update_wrapper
from debuger import *

def foxes_and_hens(strategy, foxes=2, hens=45):
    """Play the game of foxes and hens."""
    # A state is a tuple of (score-so-far, number-of-hens-in-yard, deck-of-cards)
    state = (score, yard, cards) = (0, 0, 'F'*foxes + 'H'*hens)
    while cards:
        action = strategy(state)
        state = (score, yard, cards) = do(action, state)
    return score + yard

def do(action, state):
    "Apply action to state, returning a new state."
    (score, yard, cards) = state
    if action == 'wait':
        card = random.choice(cards)
        cards = cards.replace(card,'',1)
        return (score, yard + 1,cards) if card == 'H' else (score, 0, cards)
    elif action == 'gather':
        card = random.choice(cards)
        cards = cards.replace(card,'',1)
        #cards.remove(card)
        return (score+yard,0 , cards)
    else:
        raise ValueError
    
def take5(state):
    "A strategy that waits until there are 5 hens in yard, then gathers."
    (score, yard, cards) = state
    if yard < 5:
        return 'wait'
    else:
        return 'gather'

def average_score(strategy, N=250):
    return sum(foxes_and_hens(strategy) for _ in range(N)) / float(N)

def superior(A, B=take5):
    "Does strategy A have a higher average score than B, by more than 1.5 point?"
    return average_score(A) - average_score(B) > 1.5

@memo
def strategy(state):
    (score, yard, cards) = state

    @memo
    def FH_actions(state):
        (score, yard, cards) = state
        return ['wait','gather'] if yard != 0 else ['wait']

    @memo
    def P_hen(cards):
        return cards.count('H') / (1.0*len(cards))
        
    @memo
    def P_fox(cards):
        return cards.count('F') / (1.0*len(cards))
    @trace
    @memo
    def Point(state):
        (score, yard, cards) = state
        if cards == '':
            return score + yard
        elif 'H' not in cards:
            return score + yard
        elif 'F' not in cards:
            return score + yard + len(cards)
        elif 'H' in cards and 'F' in cards:
            cards_H = cards.replace('H','',1)
            cards_F = cards.replace('F','',1)
            p_g = P_hen(cards) * Point((score+yard,0, cards_H)) + P_fox(cards) * Point((score+yard,0, cards_F))
            p_w = P_hen(cards) * Point((score, yard+1, cards_H)) + P_fox(cards) * Point((score, 0, cards_F))
            return max(p_g,p_w)

    #@memo
    #def best_action(state):
        #(score, yard, cards) = state
        #cards_H = cards.replace('H','',1)
        #cards_F = cards.replace('F','',1)
        #p_g = P_hen(cards) * Point((score+yard,0,cards_H)) + P_fox(cards) * Point((score + yard,0,cards_F))
        #p_w = P_hen(cards) * Point((score,yard+1,cards_H)) + P_fox(cards) * Point((score,0,cards_F))
        #return 'wait' if p_w > p_g else 'gather'

    @memo
    @trace
    def Q_FH(state, action, Pwin):  
        "The expected value of choosing action in state."
        (score, yard, cards) = state
        cards_H = cards.replace('H','',1)
        cards_F = cards.replace('F','',1)
        if action == 'gather':
            return P_hen(cards)* Pwin((score+yard,0,cards_H)) + P_fox(cards)*Pwin((score + yard,0,cards_F))
            #return 1 - Pwin(hold(state))
        if action == 'wait':
            return P_hen(cards)*Pwin((score,yard+1,cards_H)) + P_fox(cards)*Pwin((score,0,cards_F))
        raise ValueError

    #@trace
    @memo
    def Pwin(state):
        """The utility of a state; here just the probability that an optimal player
        whose turn it is to move can win from the current state."""
        # Assumes opponent also plays with optimal strategy.
        (score, yard, cards) = state
        if cards == '':
            return score + yard
        elif 'H' not in cards:
            return score + yard
        elif 'F' not in cards:
            return score + yard + len(cards)
        elif 'H' in cards and 'F' in cards:
            return max(Q_FH(state,action,Pwin)
                    for action in FH_actions(state))
        else:
            raise ValueError


    @memo
    def best_action(state, actions, Q, U):
        "Return the optimal action for a state, given U."
        def EU(action): return Q(state, action, U)
        return max(actions(state), key=EU)
    
    
    
    #print Pwin((42, 10, 'FH'))
    return best_action(state,FH_actions , Q_FH, Pwin)
    
    #return best_action(state)

    #print cards
    #print P_hen(cards)
    #print P_fox(cards)
def strategy2(state):
    (score, yard, cards) = state
    @memo
    def P_hen(cards):
        return cards.count('H') / (1.0*len(cards))
        
    @memo
    def P_fox(cards):
        return cards.count('F') / (1.0*len(cards))
    if 'F' not in cards:
        return 'wait'
    if yard > 3:
        return 'gather'
    if P_hen(cards) > 0.3:
        return 'wait'
    else:
        return 'gather'

    #print Point(state)


    #"Apply action to state, returning a new state."
    #(score, yard, cards) = state
    #if action == 'wait':
        #card = random.choice(cards)
        #cards = cards.replace(card,'',1)
        #return (score, yard + 1,cards) if card == 'H' else (score, 0, cards)
    #elif action == 'gather':
        #card = random.choice(cards)
        #cards = cards.replace(card,'',1)
        ##cards.remove(card)
        #return (score+yard,0 , cards)
    #else:
        #raise ValueError
    ## your code here

def test():
    gather = do('gather', (4, 5, 'F'*4 + 'H'*10))
    assert (gather == (9, 0, 'F'*3 + 'H'*10) or 
            gather == (9, 0, 'F'*4 + 'H'*9))
    
    wait = do('wait', (10, 3, 'FFHH'))
    assert (wait == (10, 4, 'FFH') or
            wait == (10, 0, 'FHH'))
    
    assert superior(strategy)
    return 'tests pass'

print test()   

#foxes=7, hens=45

#print average_score(take5) 
#print average_score(strategy2) 
print average_score(strategy)  

state = (score, yard, cards) = (0, 0, 'F'*10 + 'H'*30)
