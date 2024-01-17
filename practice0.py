# Two strings are anagrams or not
# def Solution(str1, str2):
#     if len(str1) != len(str2):
#         return 'Not an anagram'
#     else:
#         s1 = ''.join(sorted(str1))
#         s2 = ''.join(sorted(str2))
#         if s1 == s2:
#             return 'An anagram'
#         else:
#             return 'Not an anagram'
#
#
# def main():
#     str1 = input()
#     str2 = input()
#     res = Solution(str1, str2)
#     print(res)
#
#
# if __name__ == '__main__':
#     main()

# Number of occurrences of a character in a String
# def Solution(S, F):
#     count = 0
#     for i in S:
#         if i == F:
#             count += 1
#     return count
#
#
# def main():
#     string = input()
#     search = input()
#     res = Solution(string, search)
#     print(res)
#
#
# if __name__ == "__main__":
#     main()

# Pattern 544333222211111
# def Solution(n):
#     for i in range(n, 0, -1):
#         for j in range(i, n + 1):
#             print(i, end="")
#
#
# def main():
#     i = int(input())
#     res = Solution(i)
#     print(res)
#
#
# if __name__ == '__main__':
#     main()

# Matching characters code
# def Solution(s1, s2):
#     set_s1 = set(s1)
#     set_s2 = set(s2)
#     merge = set_s1 & set_s2
#     return len(merge)
#     c, j = 0, 0
#     for i in s1:
#         if s2.find(i) >= 0 and j == s1.find(i):
#           c += 1
#         j += 1
#     return c


# def main():
#     str1 = input()
#     str2 = input()
#     res = Solution(str1, str2)
#     print("Number of matching characters are: ", res)


# if __name__ == '__main__':
#     main()

# Palindrome and Reverse a String code

# def Solution(s):
#     if s == s[::-1]:
#         return "is_Palindrome"
#     else:
#         return "not_Palindrome"
#
#
# def main():
#     string = input()
#     res = Solution(string)
#     print(res)
#
#
# if __name__ == '__main__':
#     main()

# Count vowels

# def solution(productID):
#     vowels = "AaEeIiOoUu"
#     string = str(productID)
#     final = [each for each in string if each in vowels]
#
#     return len(final)
#
#     count = 0
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     for i in range(len(productID)):
#         for j in range(len(vowels)):
#             if vowels[j] == productID[i]:
#                 count += 1
#     return count
#
#
# def main():
#     productID = list(map(str, input().split()))
#     result = solution(productID)
#     print(result)
#
#
# if __name__ == '__main__':
#     main()1


# List out of bound index ( Try - Except )
# lst = [1, 2, 3, 4, 5, 6]
# try:
#     for i in range(0, len(lst)+1):
#         print(lst[i])
# except IndexError:
#     print("Index error occurred!")

# Smallest & Largest element in an array || 2nd Smallest & Largest
# || Reverse || Count frequency || sum

# arr = [9, 5, 3, 3, 3, 6, 7, 7]
# arr.sort()
# print(arr)
# print(arr[0])
# print(arr[-1])
# arr1 = [*set(arr)]
# arr1 = list(set(arr))
# print(arr)
# print(arr[-2])
# print(arr[1])
# print(arr[::-1])
# print(arr.count(3))
# print(sum(arr))

# Block swap Algorithm

# arr = list(map(int, input().split()))
# k = int(input())
# for x in range(k):
#     for i in range(len(arr)-1):
#         arr[i], arr[i-1] = arr[i-1], arr[i]
# print(arr)

# def findEarliestMonth(stockprice):
#     month = 0
#     change = max(stockPrice)
#     l = []
#     total_sum = 0
#     for i in range(len(stockPrice)):
#         total_sum += stockPrice[i]
#     left = 0
#     left_sum = 0
#     while(len(stockPrice)):
#         left = stockPrice.pop(0)
#         l.append(left)
#         left_sum += left
#         avg1 = left_sum//len(l)
#         avg2 = (total_sum-left_sum)//len(stockPrice)
#     return (abs(avg1-avg2))

# lower = 900
# upper = 1000
#
# print("Prime numbers between", lower, "and", upper, "are:")
#
# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)
#
# s = 'aabbccdd'
# r = '*'.join(s[i:i+1] for i in range(0, len(s)))
# print(r)
