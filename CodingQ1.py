def Solution(n, x, arr):
    hm = {}
    for i in range(n):
        hm.__setitem__(i, 0)
    for i in range(n):
        if arr[i] != -1:
            hm.__setitem__(arr[i], hm.get(arr[i]+1))
    print(hm)
    count = 0
    for i in range(n):
        if hm.get(i) >= x:
            count += 1
    return count


def main():
    N = int(input())
    X = int(input())
    Arr = list(map(int, input().split()))
    # print(Arr)

    result = Solution(N, X, Arr)
    print(result)


if __name__ == '__main__':
    main()
