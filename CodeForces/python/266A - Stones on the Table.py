n = int(input())
stones = input()
counter = 0
for x in range(1, n):
    if stones[x] == stones[x - 1]:
        counter += 1
print(counter)

# enumerate method

# for i, v in enumerate(stones[1:]):
#     prev = stones[i]
#     if v == prev:
#         counter += 1
