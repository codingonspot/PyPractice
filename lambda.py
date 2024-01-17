from functools import reduce

my_list = [2, 5, 8, 10, 9, 3]
my_list1 = [3, 6, 9, 11, 7, 4]
my_list2 = [1, 3, 4, 10, 12, 5]

a = map(lambda x : x * 2, my_list)
print(list(a))
b = map(lambda x, y : x + y, my_list1, my_list2)
print(list(b))

c = filter(lambda x : x%2 == 0, my_list)
print(list(c))
d = filter(lambda x : True if x>= 5 else False, my_list)
print(list(d))

e = reduce(lambda x, y : x + y, my_list)
print(e)