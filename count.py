# for string, list, tuple, dict, set
def count(data):
    c = 0
    for elem in data:
        c = c + 1
    return c


# use python define len function first

s = 'Hello, world'
print(count(s))
print(len(s))

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count(lst))
print(len(lst))

t = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
print(count(t))
print(len(t))

d = {'a': 1, 'b': 2, 'c': 3}
print(count(d))
print(len(d))

s = {1, 2, 3}
print(count(s))
print(len(s))