# ---------------
# User Instructions
#
# Write a function, findtags(text), that takes a string of text
# as input and returns a list of all the html start tags in the 
# text. It may be helpful to use regular expressions to solve
# this problem.

import re
from string import split


def findtags(text):
    return re.findall(r"<\s*[a-z]+[^'<]*>",text)
#<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)
#<\s*[A-Za-z]+\s*[^<]*>
    #USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    #matchs=XML_TAG.search(text)

    #for line in split(text, '\n'):
        #print line
        ##print USER_RE.match(text)
    
        #print XML_TAG.search(line)
     

    # your code here

testtext1 = """
My favorite website in the world is probably 
<a href="www.udacity.com">Udacity</a>. If you want 
that link to open in a <b>new tab</b> by default, you should
write <a href="www.udacity.com"target="_blank">Udacity</a>
instead!
"""

testtext2 = """
Okay, so you passed the first test case. <let's see> how you 
handle this one. Did you know that 2 < 3 should return True? 
So should 3 > 2. But 2 > 3 is always False.
"""

testtext3 = """
It's not common, but we can put a LOT of whitespace into 
our HTML tags. For example, we can make something bold by
doing <         b           > this <   /b    >, Though I 
don't know why you would ever want to.
"""

def test():
    assert findtags(testtext1) == ['<a href="www.udacity.com">', 
                                   '<b>', 
                                   '<a href="www.udacity.com"target="_blank">']
    assert findtags(testtext2) == []
    assert findtags(testtext3) == ['<         b           >']
    return 'tests pass'

print test()

print findtags(testtext1)
print findtags(testtext2)
print findtags(testtext3)
