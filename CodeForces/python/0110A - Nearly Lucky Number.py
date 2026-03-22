n = input()
lucky_nums = sum(1 for x in n if x in '47')

print('YES' if all(x in '47' for x in str(lucky_nums)) else 'NO')


# not one line solution:

# n = input()

# lucky_nums = 0
# result = 'YES'

# for x in n:
#     if x in '47':
#         lucky_nums += 1

# for num in str(lucky_nums):
#     if num not in '47':
#         result = 'NO'
#         break

# print(result)
