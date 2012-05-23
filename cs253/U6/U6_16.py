
# QUIZ implement the basic memcache functions

CACHE = {}

#return True after setting the data
def set(key, value):
    try:
        CACHE[key] = value
        return True
    except:
        return False

    ###Your set code here.

#return the value for key
def get(key):
    try:
        return CACHE[key]
    except KeyError:
        return None
    ###Your get code here.

#delete key from the cache
def delete(key):
    try:
        del CACHE[key]
    except KeyError:
        pass
    ###Your delete code here.

#clear the entire cache
def flush():
    CACHE.clear()
    ###Your flush code here.

print set('x', 1)
#>>> True

print get('x')
#>>> 1

print get('y')
#>>> None

delete('x')
print get('x')
#>>> None

