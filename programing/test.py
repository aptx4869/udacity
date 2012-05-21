from debuger import *
def P_hen(cards):
    return cards.count('H') / (1.0*len(cards))
    
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


print Point((4, 5, 'F'*4 + 'H'*10))
print Point((4, 5, 'F'*4 + 'H'*10))
print Point((4, 1, 'FFFHHHHHHHHH'))
Point((4, 0, 'FFHHHH'))

