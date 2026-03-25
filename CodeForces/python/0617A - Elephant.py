position = int(input())
counter = 0


counter += position // 5
position %= 5

counter += position // 4
position %= 4

counter += position // 3
position %= 3

counter += position // 2
position %= 2

counter += position // 1
position %= 1


print(counter)