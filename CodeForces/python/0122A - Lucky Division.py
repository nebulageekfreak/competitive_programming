n = int(input())
lucky_nums = [4, 7, 47, 74, 477, 744]

for x in lucky_nums:
    if n % x == 0:
        print('YES')
        break
else:
    print('NO')
