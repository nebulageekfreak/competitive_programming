n = int(input())
counter = 0

for x in range(n):
    people, capacity = map(int, input().split())

    if capacity - people >= 2:
        counter += 1

print(counter)
