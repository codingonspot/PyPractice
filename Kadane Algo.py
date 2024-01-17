# Kadane' Algorithm
# ***Maximum Subarray Sum*** #
def max_sarray(nums):
    if not nums:
        return 0

    max_sum = current_sums = nums[0]

    for num in nums[1:]:
        current_sums = max(num, current_sums + num)
        max_sum = max(max_sum, current_sums)

    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res = max_sarray(nums)
print(res)
