n = int(input())

for _ in range(n):
    n, c, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    for x in a:
        if c >= x:
            canUse = min(k, c - x)
            k -= canUse
            x += canUse
            c += x
    print(c)
