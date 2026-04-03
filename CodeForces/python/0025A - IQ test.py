_ = int(input())

nums = map(int, input().split())

oddNums = []
evenNums = []

for i, v in enumerate(nums):
    if v % 2 == 0:
        evenNums.append(i+1)
    else:
        oddNums.append(i+1)

print(oddNums[0] if len(oddNums) < len(evenNums) else evenNums[0])
