import itertools
from fractions import Fraction
sex = 'BG'
weeks = 'MTWtFSs'

def product(*variables):
    return map(''.join, itertools.product(*variables))

kids = product(sex,weeks,sex,weeks)

Tboy = [s for s in kids if 'BT' in s]
print Tboy

def two_boy(s): return s.count('B') == 2

def condP(predicate, event):
    pred = [s for s in event if predicate(s)]
    return Fraction(len(pred), len(event))
print condP(two_boy,Tboy)
