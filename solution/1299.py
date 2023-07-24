# 1299. Replace Elements with Greatest Element on Right Side
# https://www.youtube.com/watch?v=ZHjKhUjcsaU
arr = [17, 18, 5, 4, 6, 1]
# Output: [18,6,6,6,1,-1]
print(arr)

# intital max = -1
# iterate from the end.
# newMax = max(oldMax, arr[i])

right_max = -1

# range(start, stop, step)
# default step is 1
for i in range(len(arr) - 1, -1, -1):
    new_max = max(right_max, arr[i])
    arr[i] = right_max
    right_max = new_max

print(arr)
