def local_scope(b=0, c=0):
    global a
    # changes global a
    a = 13
    # creates new local b variable
    b = 23
    c = 30
    d = 40
    print(f'Local a({a}), b({b}), c({c}), d({d})')


a = 10
b = 20
local_scope()
print(f'Global a({a}), b({b})')