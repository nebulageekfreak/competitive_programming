n = input()
lucky_nums = sum(1 for x in n if x in '47')

print('YES' if all(x in '47' for x in str(lucky_nums)) else 'NO')
