class Solution:

    @staticmethod
    def countSol(s):
        prevSum = {}
        res = 0
        currSum = 0

        for i in range(len(s)):
            if 'A' <= S[i] <= 'Z':
                currSum += 1
            else:
                currSum -= 1

            if currSum == 0:
                res += 1

            if currSum in prevSum:
                res += prevSum[currSum]
            else:
                prevSum[currSum] = 1

        return res


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        print(ob.countSol(S))

        # substring = {s[i:j] for i in range(len(s))
        #              for j in range(i + 1, len(s) + 1)}
        # n = 0
        # res = []
        # for k in substring:
        #     if len(k) % 2 == 0:
        #         n += 1
        #         res.append(k)
        # print(n)
        #
        # return res
