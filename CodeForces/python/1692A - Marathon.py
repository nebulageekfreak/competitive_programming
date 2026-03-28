t = int(input())

for i in range(t):
    a, b, c, d = map(int, input().split())

    inFrontOfTimur = sum([b > a, c > a, d > a])

    print(inFrontOfTimur)
