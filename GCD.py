import math


class Solution:
    @staticmethod
    def solve(L, R):
        res = [L, R]
        return res


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, R = map(int, input().strip().split())
        ob = Solution()
        ans = ob.solve(L, R)

        if len(ans) != 2:
            print(-10)
        elif ans[0] == -1 and ans[1] == -1:
            print(-1)
        elif L <= ans[0] <= R and L <= ans[1] <= R:
            print(math.gcd(ans[0], ans[1]))
        else:
            print(-10)