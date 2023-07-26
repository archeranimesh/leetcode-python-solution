# 167. Two Sum II - Input Array Is Sorted
# https://www.youtube.com/watch?v=cQ1Oz4ckceM

numbers = [1, 3, 4, 5, 7, 10, 11]
target = 9
left_pointer, right_pointer = 0, len(numbers) - 1

while left_pointer < right_pointer:
    cur_sum = numbers[left_pointer] + numbers[right_pointer]

    if cur_sum > target:
        right_pointer -= 1
    elif cur_sum < target:
        left_pointer += 1
    else:
        print("\t\t target index", left_pointer, right_pointer)
        break
