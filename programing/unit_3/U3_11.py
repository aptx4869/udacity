def lit(s): return lambda text: set([text[len(s):]]) if text.startswith(s) else null

def seq(x, y): return lambda text: set().union(*map(y, x(text)))

def alt(x, y): return lambda text:set(x(text)).union(y(text))
null = frozenset([])
txt='abccdeeef'
l=lit('abc')
print l
print l(txt)
print seq(l,lit('cde'))(txt)

g = alt(lit('a'), lit('b'))
print g('abc')

