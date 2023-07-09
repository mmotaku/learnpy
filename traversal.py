# for string, list, tuple
def traversal(seq):
    for i in range(len(seq)):
        print(seq[i], end=' ')
    print()

    for elem in seq:
        print(elem, end=' ')
    print()


# for dict
def traversal_dict(d):
    for key in d:
        print(key, d[key])


# for set
def traversal_set(s):
    for elem in s:
        print(elem)


s = 'Hello, world'
traversal(s)

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
traversal(lst)

t = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
traversal(t)

d = {'a': 1, 'b': 2, 'c': 3}
traversal_dict(d)

s = {1, 2, 3}
traversal_set(s)
