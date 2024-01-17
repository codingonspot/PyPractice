def func(na):
    arr = []
    for i in range(na):
        arrele = int(input())
        arr.append(arrele)
    print(arr)
    flag = 0
    for i in range(na):
        if arr[i-1] % 2 == arr[i] % 2:
            flag = 1
            break
    if flag == 1:
        print("NO")
    if flag == 0:
        print("YES")


if __name__ == '__main__':
    n = int(input())
    for i in range (n):
        na = int(input())
        func(na)

