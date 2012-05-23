
#handy link
#http://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them
#maybe a link to itertools

SERVERS = ['SERVER1', 'SERVER2', 'SERVER3', 'SERVER4']
n = -1

# QUIZ - implement the function get_server, which returns one element from the
# list SERVERS in a round-robin fashion on each call.
def get_server():
    global n
    n=(n+1)%len(SERVERS)
    return SERVERS[n]
    
    ###Your code here.

print n
print get_server()
print n
print get_server()
print n
print get_server()

print n
# >>> SERVER1
# >>> SERVER2
# >>> SERVER3
# >>> SERVER4
# >>> SERVER1

