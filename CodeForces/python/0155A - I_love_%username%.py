_ = int(input())

nums = map(int, input().split())

first = next(nums)
currMax = first
currMin = first
counter = 0


for i in nums:
    if i > currMax:
        currMax = i
        counter += 1
    elif i < currMin:
        currMin = i
        counter += 1

print(counter)
