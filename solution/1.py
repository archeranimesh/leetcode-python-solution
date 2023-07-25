# 1. Two Sum
# https://www.youtube.com/watch?v=KLlXCFG5TnA
nums = [2, 7, 11, 15]
target = 9

length = len(nums)
i = 0
flag = False

while i < length:
    print(i, "-->", nums[i])
    j = i
    while j < length:
        print("\t", j, "==>", nums[j])
        target_sum = nums[i] + nums[j]
        if target_sum == target:
            flag = True
            print("\t\t target index", i, j)
            break
        j += 1
    if flag:
        break
    i += 1
