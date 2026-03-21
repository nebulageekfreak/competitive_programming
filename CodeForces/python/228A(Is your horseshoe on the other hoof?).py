horseshoes = set(map(int, input().split())) # using set to remove duplicate nums
print(4 - len(horseshoes))

# sorted list method

# horseshoes = sorted(list(map(int, input().split())))
# needToBuy = 0
# for i in range(1, len(horseshoes)):
#     if horseshoes[i] == horseshoes[i - 1]:
#         needToBuy += 1
#
# print(needToBuy)
