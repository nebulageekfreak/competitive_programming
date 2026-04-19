_ = int(input())

nums = list(map(int, input().split()))
maxNum = max(nums)
needToSpend = 0

for num in nums:
    if maxNum > num:
        needToSpend += maxNum - num

print(needToSpend)
