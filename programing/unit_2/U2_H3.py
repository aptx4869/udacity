# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!
def _isub(text,needle,length):
    try:
        assert needle-length >= 0
        assert needle+length <= len(text)
        #return text[needle-length].upper() == text[needle+length].upper()
        return text[needle-length] == text[needle+length]
    except:
        return False

def _ismirro(text,needle,length):
    try:
        assert needle-length >= 0
        assert needle+length <= len(text)
        #return text[needle-length+1].upper() == text[needle+length].upper()
        return text[needle-length+1]== text[needle+length]
    except:
        return False
        #enumerate
def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    text=text.upper()
    working_length=0
    mirro_length = 0
    candidate = [i for i in range(len(text))]
    candidate_record=candidate[:]
    for length in range(1,len(text)):

        #print candidate
        #print '='*10
        candidate=candidate_record[:]
        for needle in candidate:
            #print needle
            if _isub(text,needle,length):
                working_length = length
            elif _ismirro(text,needle,length):
                mirro_length = length
                #print "working is ",working_length
                #yield (length,needle)
            #elif _ismirror(text,needle,length):
                #yield (length,needle)
            else:
                #print needle
                #print candidate_record
                candidate_record.remove(needle)
                
        #print length
        if len(candidate) == 0:
            return (needle-working_length,needle+working_length+1) if working_length>mirro_length else (needle-mirro_length+1,needle+mirro_length+1)

    return (0,0)

    
def test():
    L = longest_subpalindrome_slice
    #print L('')
    #print L('Race carr')
    #print L('racecarX') 
    #print L('racecar') 
    txt = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nunc libero, venenatis id porttitor et, pharetra et urna. Donec nec velit varius massa lacinia placerat. Fusce vulputate mollis nunc, et tincidunt erat imperdiet at. Aliquam sit amet tortor in sem tempor condimentum. Curabitur vel mauris lectus. Nulla at metus ac turpis malesuada accumsan vitae et arcu. Sed semper pellentesque est quis tristique. Mauris egestas porttitor risus, lobortis accumsan ligula sollicitudin eu. Ut sollicitudin nibh ac quam viverra id euismod velit posuere. Nullam ut ultrices arcu.

Quisque et turpis massa, quis faucibus libero. Sed nulla nunc, pellentesque in congue id, dictum eget sem. Vivamus ultrices interdum velit ac pulvinar. Curabitur facilisis, purus nec commodo vulputate, purus magna dictum dolor, at fringilla arcu ante nec est. Nulla rutrum semper ullamcorper. Praesent fermentum ultrices sem id auctor. Sed eget euismod tortor. Vestibulum vestibulum, massa faucibus semper laoreet, dui arcu viverra turpis, eu rhoncus ante mauris suscipit velit. Phasellus vitae nisi molestie ligula eleifend fermentum at vel est. Aliquam quis erat massa, sit amet fringilla mi. Nulla ac dolor nisl. Pellentesque egestas felis id ante bibendum sed aliquet augue mollis. Maecenas condimentum lacinia mauris, ut egestas est bibendum quis. Donec vel sem nec turpis bibendum ultricies eget sed diam. Vestibulum sed metus vel ipsum convallis adipiscing.

Nulla eu lacus eget est pellentesque pulvinar eu nec libero. Nullam orci ligula, consectetur eget adipiscing at, scelerisque quis neque. Curabitur tempor urna ac nisi placerat nec tincidunt magna pulvinar. Praesent id congue augue. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum pretium ullamcorper dolor sit amet consectetur. Curabitur vehicula ultricies commodo. In erat massa, condimentum nec elementum id, ullamcorper in felis.

Integer nec imperdiet ante. Vestibulum pellentesque libero eget odio mollis at ullamcorper ipsum cursus. Curabitur quis justo a leo porta aliquam vitae eu nunc. In dolor sem, viverra non euismod at, auctor sit amet turpis. Phasellus convallis egestas dui, sed pharetra leo dignissim in. Praesent mi tortor, posuere ut gravida at, facilisis vel nisl. Integer orci metus, volutpat sit amet tincidunt eu, tincidunt vitae sapien. In imperdiet elementum lobortis. Vestibulum viverra augue eu urna vehicula feugiat. Aliquam sapien velit, posuere ut egestas at, bibendum nec risus. Vestibulum lacus elit, semper sit amet laoreet at, bibendum non risus.

Duis turpis dolor, tincidunt sed condimentum ut, sodales vitae eros. Morbi urna odio, eleifend at adipiscing vitae, pretium ut mi. In consequat, tellus quis scelerisque aliquam, turpis metus sagittis mi, semper dapibus sem ligula et felis. Curabitur turpis ante, pretium id mollis vitae, fringilla nec turpis. In enim ligula, porta nec posuere quis, vestibulum ac justo. Vestibulum laoreet nisi ac magna accumsan aliquet. Pellentesque sed metus bibendum enim sodales rutrum. Nullam pretium arcu quis erat eleifend tempus. Suspendisse lacinia, est nec mollis lobortis, dui leo commodo nulla, a aliquam diam orci ut mauris. Aenean non purus in eros fermentum ultrices. In at libero dolor, ut venenatis ante. Phasellus turpis quam, laoreet at porta nec, gravida a erat. Morbi purus augue, fermentum non aliquet blandit, fermentum viverra tortor. Donec consequat sodales libero et venenatis. Nam a felis non massa aliquet pharetra dictum quis erat. ingirumimusnocteetconsumimurigni"""
    L(txt)
    
    #print L('Race carr') 
    #assert L('racecar') == (0, 7)
    #assert L('Racecar') == (0, 7)
    #assert L('RacecarX') == (0, 7)
    #assert L('Race carr') == (7, 9)
    #assert L('') == (0, 0)
    #assert L('something rac e car going') == (8,21)
    #assert L('xxxxx') == (0, 5)
    #assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

#print _isub('racecar',3,2)
#print _isub('racecar',3,3)
#print _isub('racecarX',3,4)
#print test()

txt = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nunc libero, venenatis id porttitor et, pharetra et urna. Donec nec velit varius massa lacinia placerat. Fusce vulputate mollis nunc, et tincidunt erat imperdiet at. Aliquam sit amet tortor in sem tempor condimentum. Curabitur vel mauris lectus. Nulla at metus ac turpis malesuada accumsan vitae et arcu. Sed semper pellentesque est quis tristique. Mauris egestas porttitor risus, lobortis accumsan ligula sollicitudin eu. Ut sollicitudin nibh ac quam viverra id euismod velit posuere. Nullam ut ultrices arcu.

Quisque et turpis massa, quis faucibus libero. Sed nulla nunc, pellentesque in congue id, dictum eget sem. Vivamus ultrices interdum velit ac pulvinar. Curabitur facilisis, purus nec commodo vulputate, purus magna dictum dolor, at fringilla arcu ante nec est. Nulla rutrum semper ullamcorper. Praesent fermentum ultrices sem id auctor. Sed eget euismod tortor. Vestibulum vestibulum, massa faucibus semper laoreet, dui arcu viverra turpis, eu rhoncus ante mauris suscipit velit. Phasellus vitae nisi molestie ligula eleifend fermentum at vel est. Aliquam quis erat massa, sit amet fringilla mi. Nulla ac dolor nisl. Pellentesque egestas felis id ante bibendum sed aliquet augue mollis. Maecenas condimentum lacinia mauris, ut egestas est bibendum quis. Donec vel sem nec turpis bibendum ultricies eget sed diam. Vestibulum sed metus vel ipsum convallis adipiscing.

Nulla eu lacus eget est pellentesque pulvinar eu nec libero. Nullam orci ligula, consectetur eget adipiscing at, scelerisque quis neque. Curabitur tempor urna ac nisi placerat nec tincidunt magna pulvinar. Praesent id congue augue. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum pretium ullamcorper dolor sit amet consectetur. Curabitur vehicula ultricies commodo. In erat massa, condimentum nec elementum id, ullamcorper in felis.

Integer nec imperdiet ante. Vestibulum pellentesque libero eget odio mollis at ullamcorper ipsum cursus. Curabitur quis justo a leo porta aliquam vitae eu nunc. In dolor sem, viverra non euismod at, auctor sit amet turpis. Phasellus convallis egestas dui, sed pharetra leo dignissim in. Praesent mi tortor, posuere ut gravida at, facilisis vel nisl. Integer orci metus, volutpat sit amet tincidunt eu, tincidunt vitae sapien. In imperdiet elementum lobortis. Vestibulum viverra augue eu urna vehicula feugiat. Aliquam sapien velit, posuere ut egestas at, bibendum nec risus. Vestibulum lacus elit, semper sit amet laoreet at, bibendum non risus.

Duis turpis dolor, tincidunt sed condimentum ut, sodales vitae eros. Morbi urna odio, eleifend at adipiscing vitae, pretium ut mi. In consequat, tellus quis scelerisque aliquam, turpis metus sagittis mi, semper dapibus sem ligula et felis. Curabitur turpis ante, pretium id mollis vitae, fringilla nec turpis. In enim ligula, porta nec posuere quis, vestibulum ac justo. Vestibulum laoreet nisi ac magna accumsan aliquet. Pellentesque sed metus bibendum enim sodales rutrum. Nullam pretium arcu quis erat eleifend tempus. Suspendisse lacinia, est nec mollis lobortis, dui leo commodo nulla, a aliquam diam orci ut mauris. Aenean non purus in eros fermentum ultrices. In at libero dolor, ut venenatis ante. Phasellus turpis quam, laoreet at porta nec, gravida a erat. Morbi purus augue, fermentum non aliquet blandit, fermentum viverra tortor. Donec consequat sodales libero et venenatis. Nam a felis non massa aliquet pharetra dictum quis erat. ingirumimusnocteetconsumimurigni"""

def lorem(txt):
    print "text length:", len(txt)
    best = longest_subpalindrome_slice(txt)
    print "best palindrome found:", txt[best[0]:best[1]],  " position:", best,
import cProfile
cProfile.run('lorem(txt)')

