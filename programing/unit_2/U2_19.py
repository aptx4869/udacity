def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers)) 

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    if isinstance(n,int):
        times = [timedcall(fn,*args)[0] for _ in range(n)]
    else:
        times = []
        total_time=0
        while True:
            time=timedcall(fn,*args)[0]
            total_time+=time
            times.append(time)
            if total_time >= n:
                break

    # Your code here.
    return min(times), average(times), max(times)

