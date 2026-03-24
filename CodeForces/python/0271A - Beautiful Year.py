year = int(input())
beautifulYear = year + 1

while len(set(str(beautifulYear))) != 4:
    beautifulYear += 1
print(beautifulYear)