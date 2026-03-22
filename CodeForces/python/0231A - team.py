n  = int(input())
counter = 0
for i in range(n):
    desicion = sum(map(int, input().split()))
    if desicion >= 2:
        counter += 1
print(counter)
