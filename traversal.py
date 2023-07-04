# for string
def traversal_str(s):
    for i in range(len(s)):
        print(s[i], end=' ')
    print()

    for elem in s:
        print(elem, end=' ')
    print()


# for list
def traversal_list(lst):
    for i in range(len(lst)):
        print(lst[i], end=' ')
    print()

    for elem in lst:
        print(elem, end=' ')
    print()


# for tuple
def traversal_tuple(t):
    for i in range(len(t)):
        print(t[i], end=' ')
    print()

    for elem in t:
        print(elem, end=' ')
    print()


# for map
def traversal_map(m):
    for key in m:
        print(key, m[key])


# for set
def traversal_set(s):
    for elem in s:
        print(elem)


s = 'Hello, world'
traversal_str(s)

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
traversal_list(lst)

t = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
traversal_tuple(t)

m = {'a': 1, 'b': 2, 'c': 3}
traversal_map(m)

s = {1, 2, 3}
traversal_set(s)
