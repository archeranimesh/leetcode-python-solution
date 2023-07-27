# 53. Maximum Subarray
# https://www.youtube.com/watch?v=5WZl3MMT0Eg

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [-1]


def maxSubArray(nums) -> int:
    length = len(nums)
    i = 0
    sum_outer = float("-inf")

    while i < length:
        j = i
        print("i = ", nums[i])
        while j < length:
            print("\tj= ", nums[j])
            k = i
            j += 1
            sum_inner = 0
            while k < j:
                print("\t\tk = ", nums[k], sum_inner, sum_outer)
                sum_inner += nums[k]
                if sum_inner > sum_outer:
                    sum_outer = sum_inner
                print("\t\t[2]k = ", nums[k], sum_inner, sum_outer)

                k += 1
        i += 1
    return sum_outer


print("SUM = ", maxSubArray(nums))
