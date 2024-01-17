def nxt_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    n = int(input("Enter the number of elements in list: "))
    l1 = []
    for i in range(n):
        l1.append(int(input()))
    print(f"OUTPUT LIST: {[l1[i] if l1[i]<10 else nxt_palindrome(l1[i]) for i in range(n)]}")


    # l2 = []
    # for i in l1:
    #     if i >= 10:
    #         l2.append(nxt_palindrome(i))
    #     else:
    #         l2.append(i)
    # print(f"Output list: {l2}")
