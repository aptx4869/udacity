def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    # Your code here.
    i = 0
    while True:
        yield i
        i = (-i + 1) if i <= 0 else -1

