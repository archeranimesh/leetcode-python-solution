# 167. Two Sum II - Input Array Is Sorted
# https://www.youtube.com/watch?v=cQ1Oz4ckceM

nums = [1, 3, 4, 5, 7, 10, 11]
target = 9

length = len(nums)
i = 0
flag = False
exit_flag = False
while i < length:
    print(i, "-->", nums[i])
    j = i
    while j < length:
        print("\t", j, "==>", nums[j])
        total = nums[i] + nums[j]
        if total == target:
            print("\t\t target index", i, j)
            exit_flag = True
            flag = True
        elif total > target:
            flag = True
        if flag:
            flag = False
            break
        j += 1

    i += 1
    if exit_flag:
        break
