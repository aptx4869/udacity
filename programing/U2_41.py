word='abcde'
t=''
f=lambda x,i:x+'*'+str(10**-i)+'+'
lis=(f(word[i],i) for i in range(0,-len(word),-1))
for i in range(-1,-len(word)-1,-1) :
    t+=f(word[i],i)
t=t[:-1]
enumerate
print t
print ''.join(lis)
print sum(lis)
def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    f=lambda x,i:str(10**(-i-1))+'*'+x+'+'
    lis=(f(word[i],i) for i in range(-1,-len(word)-1,-1))
    t=''.join(lis)
    return t[:-1]

print compile_word('YOU')
#def compile_word(word):
    #"""Compile a word of uppercase letters as numeric digits.
    #E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    #Non-uppercase words unchanged: compile_word('+') => '+'"""
    ## Your code here.
    #t=''
    #f=lambda x,i:x+'*'+str(10**-i)+'+'
    #lis=(f(word[i],i) for i in range(0,-len(word),-1))
    #t=''.join(lis)
    #return t[:-1]
    #for i in range(0,-len(word),-1) :
        #t+=f(word[i],i)
    #t=t[:-1]
    #return t
        ##t.append(word[i]+'

##f=lambda  : word[i]+'10**-i'

