games = input()
print('YES' if ('1' * 7) in games or ('0' * 7) in games else 'NO')


# another method to solve this
#
#
# games = input()
# counter = 1
# found = False
#
# for x in range(1, len(games)):
#     if x == games[x-1]:
#         counter += 1
#         if counter == 7:
#             found = True
#             break
#     else:
#         counter = 1
#
# print("YES" if found else "NO")
