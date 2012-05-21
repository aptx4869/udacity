# -----------
# User Instructions
# 
# Define a function, kind(n, ranks).

def kind(n, ranks):
    ranks.sort(reverse = True)
    for i in range(len(ranks)-n+1):
        a=len(set(ranks[i:i+n]))==1
        if i+n+1<len(ranks):
            b=len(set(ranks[i:i+n+1]))>1
        else:
            b=True
        if i>0:
            c=len(set(ranks[i-1:i+n]))>1
        else:
            c=True
        if a and b and c:
            return ranks[i]
    return None
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    # Your code here.
    
def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    fkranks = card_ranks(fk)
  #  tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    return 'tests pass'
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks

test()
