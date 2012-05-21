# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the 
# non-negative numbers. The runtime of your program should be 
# proportional to the LOGARITHM of the input. You may want to 
# do some research into binary search and Newton's method to 
# help you out.
#
# This function should return another function which computes the
# inverse of the input function. 
#
# Your inverse function should also take an optional parameter, 
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The 
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is 
# efficient enough. 

def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1 

def inverse(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x_1=0.
        x_2=1.
        x_m=(x_1+x_2)/2
        y_1,y_2,y_m=f(x_1),f(x_2),f(x_m)
        while (y - y_1) > delta/1024.:
            if y_2 < y:
                x_m = x_2
                x_2 =2.0 * x_m -x_1
            elif y_m < y:
                x_1=x_m
                x_m=(x_1+x_2)/2.0
            else:
                x_2=x_m
                x_m=(x_1+x_2)/2.0
            y_1,y_2,y_m=f(x_1),f(x_2),f(x_m)

        return x_1 if (f(x_1)-y < y-f(x_1-delta)) else x_1-delta
    return f_1
        
    
def square(x): return x*x
sqrt = slow_inverse(square)
sqrt2 = inverse(square)

#print sqrt(1000000000)
print sqrt2(1000000000)

