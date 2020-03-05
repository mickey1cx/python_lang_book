a = reversed('hello')
print(a)
print(*a)

b = (1, 2, 3, 2)   # tuple
# b[2] = 4 - only read
print(b)
print(*b)

c = [1, 2, 3, 3]   # list
c[3] = 4
print(c)
print(*c)

d = {1, 2, 3, 3}   # set - unique values
print(d)
print(*d)

e = {1: 'one', 2: 'two'}    # dict
print(e)
print(*e)
print(e[1])
