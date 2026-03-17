num, operations = map(int, input().split())

for _ in range(operations):
    if num % 10 != 0:
        num -= 1
    else:
        num = num // 10
print(num)

# str method (which is slower than 1-st variant)
# for _ in range(operations):
#     if str(num)[-1] != '0':
#         num -= 1
#     else:
#         num = int(str(num)[:-1])
# print(num)
