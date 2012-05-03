#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools
def adjacent(a,b):
    return abs(a-b)==1

def floor_puzzle():
    # Your code here
    hourses = buttom,_,_,_,top = [1,2,3,4,5]
    orders = list(itertools.permutations(hourses))
    middle_order= list(itertools.permutations(hourses[1:-1])
    boundary_order = list(itertools.permutations([1,5])
    Hopper, Kay, Liskov, Perlis, Ritchie = next((Hopper, Kay, Liskov, Perlis, Ritchie) for Kay in [2,3,4,5] for Hopper in [1,2,3,4
    if Hopper != top
    if Kay != buttom
    if Liskov != buttom
    if Liskov != top
    if Perlis > Kay
    if not adjacent(Kay,Liskov)
    if not adjacent(Ritchie,Liskov)
    )
    return [Hopper, Kay, Liskov, Perlis, Ritchie]
print floor_puzzle()
Hopper, Kay, Liskov, Perlis, Ritchie = 3, 2, 4, 5 ,1
