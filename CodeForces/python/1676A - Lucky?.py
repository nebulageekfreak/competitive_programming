n = int(input())

for i in range(n):
    ticket = input()
    
    sum1 = sum(int(x) for x in ticket[:3])
    sum2 = sum(int(x) for x in ticket[3:])
    
    print("YES" if sum1 == sum2 else "NO")
