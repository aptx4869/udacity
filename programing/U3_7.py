#---------------
# User Instructions
#
# Fill out the API by completing the entries for alt, 
# star, plus, and eol.


def lit(string):  return ('lit', string)
def seq(x, y):    return ('seq', x, y)
def alt(x, y):    return ('alt', x, y)# ??
def star(x):      return ('star', x)# ??
#def plus(x):      return ('plus', x)# ??
def plus(x):      return seq(lit(x),star(lit(x)))
def opt(x):       return alt(lit(''), x) #opt(x) means that x is optional
def oneof(chars): return ('oneof', tuple(chars))
dot = ('dot',)
eol = ('eol',)#??

def test():
    assert lit('abc')         == ('lit', 'abc')
    assert seq(('lit', 'a'), 
               ('lit', 'b'))  == ('seq', ('lit', 'a'), ('lit', 'b'))
    assert alt(('lit', 'a'), 
               ('lit', 'b'))  == ('alt', ('lit', 'a'), ('lit', 'b'))
    #print star(('lit', 'a'))
    #print ('star', ('lit', 'a'))
    #print star(('lit', 'a')) == ('star', ('lit', 'a'))
    assert star(('lit', 'a')) == ('star', ('lit', 'a'))
    print plus(('lit', 'c')) #== ('seq', ('lit', 'c'), ('star', ('lit', 'c')))
    assert plus(('lit', 'c')) == ('seq', ('lit', 'c'), 
                                  ('star', ('lit', 'c')))
    assert opt(('lit', 'x'))  == ('alt', ('lit', ''), ('lit', 'x'))
    assert oneof('abc')       == ('oneof', ('a', 'b', 'c'))
    return 'tests pass'

print test()

