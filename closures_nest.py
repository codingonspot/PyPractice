def pop(li):
    def get_last_item(my_list):
        return my_list[len(li) - 1]

    li.remove(get_last_item(li))
    return li


a = [1, 2, 3, 4, 5, 6]
print(pop(a))
print(pop(a))
print(pop(a))

# def nth_power(exp):
#     def pow_of(b):
#         return pow(b, exp)
#
#     return pow_of
#
#
# square = nth_power(2)
# print(square(2))
