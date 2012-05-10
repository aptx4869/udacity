# ---------------
# User Instructions
#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function. 

def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        if len(args):
            return f(x,n_ary_f(*args))
        else:
            return x
            
        
        # your code here
    return n_ary_f

def f(x,y):return x+y

k=n_ary(f)
print k(1,2,3,4)
