from time import time


def timing(func):
    def wrapper_func(*args, **kwargs):
        start = time()
        print(start)
        result = func(*args, **kwargs)
        end = time()
        print(end)
        print('Elapsed time: {}'.format(end - start))
        return result

    return wrapper_func


@timing
def my_func(num):
    s = 0
    for i in range(num + 1):
        s += i

    return s


print(my_func(2000000))
