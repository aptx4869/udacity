import time

# complex_computation() simulates a slow function. time.sleep(n) causes the
# program to pause for n seconds. In real life, this might be a call to a
# database, or a request to another web service.
def complex_computation(a, b):
    time.sleep(.5)
    return a + b

# QUIZ - Improve the cached_computation() function below so that it caches
# results after computing them for the first time so future calls are faster
cache = {}
def cached_computation(a, b):
    try:
        return cache[(a,b)]
    except KeyError:
        cache[(a,b)]=complex_computation(a,b)
        
        return cache[(a,b)]
    ###Your code here.

#start_time = time.time()
#print cached_computation(5, 3)
#print "the first computation took %f seconds" % (time.time() - start_time)

#start_time2 = time.time()
#print cached_computation(5, 3)
#print "the second computation took %f seconds" % (time.time() - start_time2)


