n = int(input())

for i in range(n):
    nums = sorted(list(map(int, input().split())))
    
    for i in range(len(nums) - 1):
        nums[i] = nums[i] * -1
        
    print(sum(nums))
    
    
        
    
    