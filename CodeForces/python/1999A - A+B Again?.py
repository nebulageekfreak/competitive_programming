n = int(input())

for i in range(n):
    num = int(input())
    numSum = sum(int(x) for x in str(num))
    print(numSum)

