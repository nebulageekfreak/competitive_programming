red, blue = map(int, input().split())

diffSocksDays = 0
days = 0

while red > 0 or blue > 0:

    if red and blue:
        diffSocksDays += 1
        red -= 1
        blue -= 1
    elif red > 1:
        days += 1
        red -= 2
    elif blue > 1:
        days += 1
        blue -= 2
    else:
        break
    



print(diffSocksDays, days)
