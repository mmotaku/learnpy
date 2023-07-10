# for list, tuple, dict, set
def my_sum(data):
    sum = 0
    for elem in data:
        sum = sum + elem
    return sum


# use python define sum function first

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(lst))
print(my_sum(lst))

t = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
print(sum(t))
print(my_sum(t))

d = {0: 1, 1: 2, 2: 3}
print(sum(d))
print(my_sum(d))

s = {1, 2, 3}
print(sum(s))
print(my_sum(s))