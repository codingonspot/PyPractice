def list_gen(list):
    for i in list:
        yield i


a = [1, 2, 3, 4, 5, 6]
myList = list_gen(a)

for x in myList:
    print(x)
