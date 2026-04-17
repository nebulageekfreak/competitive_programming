t = int(input())

for i in range(t):
    sticks = list(map(int, input().split()))
    
    equal = sum(1 for stick in sticks if sticks[0] == stick)
    
    print('YES' if equal == 4 else 'NO')
