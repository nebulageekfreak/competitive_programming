n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

if len(set(p[1:] + q[1:])) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")