def nxt_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    n = int(input("Number of inputs you wanna check: "))
    a = []
    for i in range(n):
        t = int(input())
        a.append(t)
    for i in range(n):
        print(f"Next palindrome for {a[i]} is {nxt_palindrome(a[i])}")
