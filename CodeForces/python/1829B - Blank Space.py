t = int(input())

for _ in range(t):
    length = int(input())
    nums = map(int, input().split())

    longest = 0
    currZerosCounter = 0

    for operation in nums:
        if operation == 0:
            currZerosCounter += 1
        else:
            currZerosCounter = 0

        if currZerosCounter > longest:
            longest = currZerosCounter

    print(longest)

