given_string = "I think %s is a perfectly normal thing to do in public."
def sub1(s):
    return given_string % s
print sub1('runing')

# User Instructions
# 
# Write a function 'sub2' that, given two 
# strings, embeds those strings in the string: 
# "I think X and Y are perfectly normal things to do in public."
# where X and Y are replaced by the given 
# strings.
#

given_string2 = "I think %s and %s are perfectly normal things to do in public."
def sub2(s1, s2):
    return given_string2 % (s1,s2)

print sub2('runing','uh,')
# sub2("running", "sleeping") 
# => "I think running and sleeping are perfectly normal things to do in public."
# sub2("sleeping", "running") 
# => "I think sleeping and running are perfectly normal things to do in public."

