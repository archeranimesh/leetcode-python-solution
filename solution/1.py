# 1. Two Sum
# https://www.youtube.com/watch?v=KLlXCFG5TnA
# it will be O(n) for time and O(n) in space, as a hashmap is created.
nums = [2, 7, 11, 15]
target = 9

prev_map = {}

for i, n in enumerate(nums):
    diff = target - n
    if diff in prev_map:
        print(prev_map[diff], i)
    prev_map[n] = i
