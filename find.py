# for string
def find_str(s, substr):
    # first choice
    return substr in s


def find_char(s, c):
    # second choice, traversal to find
    for elem in s:
        if elem == c:
            return True
    return False


# for list
def find_value_list(lst, value):
    # first choice
    return value in lst

    # second choice, traversal to find
    # for elem in lst:
    #     if elem == value:
    #         return True
    # return False


# for tuple
def find_value_tuple(t, value):
    # first choice
    return value in t

    # second choice, traversal to find
    # for elem in t:
    #     if elem == value:
    #         return True
    # return False


# for map
def find_key_map(m, key):
    # first choice
    return key in m

    # second choice, traversal to find
    # for k in m:
    #     if k == key:
    #         return True
    # return False


# for map
def find_value_map(m, value):
    for k in m:
        if m[k] == value:
            return True
    return False


# for set
def find_value_set(s, value):
    # first choice
    return value in s

    # second choice, traversal to find
    # for elem in s:
    #     if elem == value:
    #         return True
    # return False


s = 'Hello, world'
print(find_str(s, 'world'))
print(find_str(s, 'mmzhudao'))

print(find_char(s, ','))
print(find_char(s, '!'))

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(find_value_list(lst, 0))
print(find_value_list(lst, 10))

t = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
print(find_value_tuple(t, 10))
print(find_value_tuple(t, 20))

m = {'a': 1, 'b': 2, 'c': 3}
print(find_key_map(m, 'a'))
print(find_key_map(m, 'd'))

print(find_value_map(m, 3))
print(find_value_map(m, 4))

s = {1, 2, 3}
print(find_value_set(s, 1))
print(find_value_set(s, 4))
