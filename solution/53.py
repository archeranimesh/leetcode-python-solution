# 53. Maximum Subarray
# https://www.youtube.com/watch?v=5WZl3MMT0Eg

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [-1]


def maxSubArray(nums) -> int:
    max_sum = nums[0]
    current_sum = 0
    for num in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += num
        max_sum = max(current_sum, max_sum)

    return max_sum


print("SUM = ", maxSubArray(nums))
