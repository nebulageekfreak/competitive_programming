n = int(input())
dct = {}
for i in range(n):
    nickname = input()
    if nickname not in dct:
        print("OK")
        dct[nickname] = 1
    else:
        print(f"{nickname}{dct[nickname]}")
        dct[nickname] += 1;

    