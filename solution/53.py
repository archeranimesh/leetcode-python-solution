# 53. Maximum Subarray
# https://www.youtube.com/watch?v=5WZl3MMT0Eg

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [-1]


def maxSubArray(nums) -> int:
    max_sum = float("-inf")
    current_sum = 0
    for num in nums:
        current_sum += num
        print("nums ", num, " sum= ", current_sum)
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
        print("\tnums ", num, " sum= ", current_sum)

    return max_sum


print("SUM = ", maxSubArray(nums))
