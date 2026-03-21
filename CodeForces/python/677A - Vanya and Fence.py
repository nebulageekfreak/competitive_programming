_, fenceHeight = map(int, input().split())
boys = map(int, input().split())

roadWidth = sum(1 if fenceHeight >= boy else 2 for boy in boys)
print(roadWidth)

# long solution
# roadWidth = 0
# for boy in boys:
#     if fenceHeight >= boy:
#         roadWidth += 1
#     else:
#         roadWidth += 2
#
# print(roadWidth)
