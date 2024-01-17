import math


class Solution(int):
    @staticmethod
    def reduction(n):
        count = 1

        maxPrime = -1
        while n % 2 == 0:
            maxPrime = 2
            n >>= 1
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                maxPrime = i
                n = n / i
        if n > 2:
            maxPrime = n
        maxp = maxPrime
        n = maxp
        while n != 0:
            n -= 1
            count += 1
        return count


def main():
    i = int(input())
    res = Solution(i)
    print(res)


if __name__ == '__main__':
    main()
