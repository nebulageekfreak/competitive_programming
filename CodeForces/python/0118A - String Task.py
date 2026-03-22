string = input().lower()
print(''.join('.' + x for x in string if x not in 'aoyuei'))


# not one line solution:
# string = input().lower()
# result = ''
# for x in string:
#     if x not in "aoyuei":
#         result += '.' + x
#
# print(result)
