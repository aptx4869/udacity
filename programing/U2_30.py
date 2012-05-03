import string, re 

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for form in fill_in(formula):
        if valid(form):
            return form
    return None
    # Your code here
    
# assume: def fill_in(formula):
#        "Generate all possible fillings-in of letters in formula with digits."
    
def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

